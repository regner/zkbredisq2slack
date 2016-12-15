

import os
import json
import logging
import requests

from time import sleep
from eveimageserver import get_image_server_link


logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

ZKILLBOARD_REDISQ = os.environ.get('REDISQ_URL', 'http://redisq.zkillboard.com/listen.php')
WATCH_IDS = set(int(x) for x in os.environ.get('WATCH_IDS', '98319972').split(','))


def find_entity_ids(entity):
    ids = set()

    if 'character' in entity:
        ids.add(entity['character']['id'])

    if 'corporation' in entity:
        ids.add(entity['corporation']['id'])

    if 'alliance' in entity:
        ids.add(entity['alliance']['id'])

    if 'faction' in entity:
        ids.add(entity['faction']['id'])

    if 'shipType' in entity:
        ids.add(entity['shipType']['id'])

    if 'weaponType' in entity:
        ids.add(entity['weaponType']['id'])

    return ids


def find_attacker_ids(killmail):
    ids = set()

    for attacker in killmail['attackers']:
        ids = ids.union(find_entity_ids(attacker))

    return ids


def format_killmail_message(zkb_data, kill):
    killmail = zkb_data['killmail']

    if 'character' in killmail['victim']:
        victim_name = killmail['victim']['character']['name']
    else:
        victim_name = killmail['victim']['shipType']['name']

    victim_corp = killmail['victim']['corporation']['name']

    if 'character' in killmail['attackers'][0]:
        killer_name = killmail['attackers'][0]['character']['name']
    elif 'shipType' in killmail['attackers'][0]:
        killer_name = killmail['attackers'][0]['shipType']['name']
    else:
        killer_name = 'Unknown'

    if 'corporation' in killmail['attackers'][0]:
        killer_corp = killmail['attackers'][0]['corporation']['name']
    elif 'faction' in killmail['attackers'][0]:
        killer_corp = killmail['attackers'][0]['faction']['name']
    else:
        killer_corp = 'Unknown'

    title = '{} ({}) killed {} ({})'.format(killer_name, killer_corp, victim_name, victim_corp)

    damage_taken = {
        'title': 'Damage taken',
        'value': '{:,}'.format(killmail['victim']['damageTaken']),
        'short': True,
    }

    attacker_count = {
        'title': 'Pilots involved',
        'value': killmail['attackerCount'],
        'short': True,
    }

    value = {
        'title': 'Value',
        'value': '{:,.2f} ISK'.format(zkb_data['zkb']['totalValue']),
        'short': True,
    }

    location = {
        'title': 'Location',
        'value': '<https://zkillboard.com/system/{}/|{}>'.format(killmail['solarSystem']['id'], killmail['solarSystem']['name']),
        'short': True,
    }

    ship = {
        'title': 'Ship',
        'value': killmail['victim']['shipType']['name'],
        'short': True,
    }

    if kill is True:
        color = 'good'

    else:
        color = 'danger'

    return {
        'attachments': [
            {
                'title': title,
                'color': color,
                'fallback': title,
                'title_link': 'https://zkillboard.com/kill/{}/'.format(zkb_data['killID']),
                'thumb_url': get_image_server_link(killmail['victim']['shipType']['id'], 'type', 64),
                'fields': [
                    damage_taken,
                    attacker_count,
                    value,
                    ship,
                    location,
                ],
            }
        ]
    }


def process_killmail(zkb_data, slack_webhook):
    formatted_slack_message = None

    found_ids = find_attacker_ids(zkb_data['killmail'])
    intersection = found_ids.intersection(WATCH_IDS)

    if len(intersection) > 0:
        logger.info('Found matching IDs indicating a kill on killmail ID {}'.format(zkb_data['killID']))
        formatted_slack_message = format_killmail_message(zkb_data, kill=True)

    else:
        found_ids = find_entity_ids(zkb_data['killmail']['victim'])
        intersection = found_ids.intersection(WATCH_IDS)

        if len(intersection) > 0:
            logger.info('Found matching IDs indicating a loss on killmail ID {}'.format(zkb_data['killID']))
            formatted_slack_message = format_killmail_message(zkb_data, kill=False)

    if formatted_slack_message:
        logger.info('Sending a Slack message for killmail ID {}'.format(zkb_data['killID']))

        requests.post(slack_webhook, data=json.dumps(formatted_slack_message))

    else:
        logger.info('Did not find any matching IDs in killmail ID {}'.format(zkb_data['killID']))


def get_killmail():
    try:
        return requests.get(ZKILLBOARD_REDISQ)

    except requests.exceptions.ConnectionError:
        logger.info('Got a connection reset error from zKillboard. Continuing on with life.')


def check_response_for_killmail(response):
    data = response.json()

    if data['package'] is not None:
        zkb_data = data['package']

        logger.info('Got new killmail with ID {}.'.format(zkb_data['killID']))

        return zkb_data

    else:
        logger.info('No new killmail.')


def run(slack_webhook):
    if slack_webhook is None:
        raise ValueError('The SLACK_WEBHOOK environment variable is not set. This must be set to continue')

    response = get_killmail()

    if response.status_code == requests.codes.ok:
        killmail = check_response_for_killmail(response)
        
        if killmail is not None:
            process_killmail(killmail, slack_webhook)

    else:
        logger.error('Problem with zKB response. Got code {}.'.format(response.status_code))
        sleep(1)


if __name__ == '__main__':
    slack_webhook = os.environ.get('SLACK_WEBHOOK')

    while True:
        run(slack_webhook)
