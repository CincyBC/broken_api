def slack_message(channel, message):
    import os
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError

    slack_token = os.environ["SLACK_TOKEN"]
    client = WebClient(token=slack_token)

    try:
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        assert e.response["error"]
