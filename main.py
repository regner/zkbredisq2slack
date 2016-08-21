

import os
import json
import logging
import requests

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

ZKILLBOARD_REDISQ = os.environ.get('REDISQ_URL', 'http://redisq.zkillboard.com/listen.php')
WATCH_IDS = set(os.environ.get('WATCH_IDS', '98319972').split(','))
SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK', 'https://hooks.slack.com/services/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')


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
        color = 'green'

    else:
        color = 'red'

    return {
        'attachments': [
            {
                'title': title,
                'color': color,s
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


def process_killmail(zkb_data):
    found_ids = find_attacker_ids(zkb_data['killmail'])

    intersection = found_ids.intersection(WATCH_IDS)
    formatted_slack_message = None

    if len(intersection) > 0:
        formatted_slack_message = format_killmail_message(zkb_data, kill=True)

    else:
        found_ids = find_entity_ids(zkb_data['killmail']['victim'])
        intersection = found_ids.intersection(WATCH_IDS)

        if len(intersection) > 0:
            formatted_slack_message = format_killmail_message(zkb_data, kill=False)

    if formatted_slack_message:
        response = requests.post(SLACK_WEBHOOK, data=json.dumps(formatted_slack_message))


def run:
    while True:
        response = requests.get(ZKILLBOARD_REDISQ)

        if response.status_code == requests.codes.ok:
            data = response.json()
            
            if data['package'] is not None:
                zkb_data = data['package']

                logger.info('Publishing new killmail with ID {}.'.format(zkb_data['killID']))

                process_killmail(zkb_data)
            
            else:
                logger.info('No new killmail.')
        
        else:
            logger.error('Problem with zKB response. Got code {}.'.format(response.status_code))


if __name__ == '__main__':
    run()
