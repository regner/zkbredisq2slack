

import json
import pytest
import responses
import sample_data

from main import run


@responses.activate
def test_attacker():
    responses.add(
        responses.GET,
        'http://redisq.zkillboard.com/listen.php',
        body=sample_data.ATTACKER,
        status=200,
        content_type='application/json'
    )

    responses.add(
        responses.POST,
        'https://hooks.slack.com/services/some/web/hook',
    )

    run('https://hooks.slack.com/services/some/web/hook')

    assert len(responses.calls) == 2
    assert json.loads(responses.calls[1].request.body) == json.loads(sample_data.ATTACKER_SLACK)


@responses.activate
def test_victim():
    responses.add(
        responses.GET,
        'http://redisq.zkillboard.com/listen.php',
        body=sample_data.VICTIM,
        status=200,
        content_type='application/json'
    )

    responses.add(
        responses.POST,
        'https://hooks.slack.com/services/some/web/hook',
    )

    run('https://hooks.slack.com/services/some/web/hook')

    assert len(responses.calls) == 2
    assert json.loads(responses.calls[1].request.body) == json.loads(sample_data.VICTIM_SLACK)


def test_exception_when_no_webhook_url():
    """Ensure we raise an exception when no webhook URL is provided"""
    with pytest.raises(ValueError):
        run(None)
