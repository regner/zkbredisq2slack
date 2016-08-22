# zkbredisq2slack
Yet another script for getting Slack messages about killmails thgat appear on zKillboard. The big advantage of this one over the others, at least all the others I could find, is that it pullsn killmails from the zKillboard RedisQ instead of from the zKillboard API. API pages from zKillboard are cached and the RedisQ pushes killmails out as they come in. The end result is that killmails get posted to Slack as soon (or very fucking close to) as they get posted to zKillboard.

## Running it
You have a few ways to run this script. The easiest, if you have Docker, is to simply run the following:

    docker run -d -e SLACK_WEBHOOK=https://hooks.slack.com/web/hook/url/here regner/zkbredisq2slack

### Environment Variables
* **SLACK_WEBHOOK:** Required. The webhook URL generated by Slack and pointing to the channel you want the messages to go to.
* **WATCH_IDS:** Required. A comma seperated list of IDs you would like to watch for. This can be character, corporation, alliance, faction, ship type ID, or even weapon type ID.
* **ZKILLBOARD_REDISQ:** Only here incase Squizz changes the URL and someone running the script doesn't want to wait for a new release of the code.
