from telethon import TelegramClient, events
import logging

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Replace with your own values
api_id = " "
api_hash = " "
group_chat_id1 = 
group_chat_id2 = 
original_number = " "
new_number = " "
user1_id = " "
user2_id = " "

# Create a new TelegramClient with your API credentials
original_client = TelegramClient("original_session", api_id, api_hash)
new_client = TelegramClient("new_session", api_id, api_hash)


# Define an event handler for new messages in the group chat
@original_client.on(events.NewMessage(chats=(group_chat_id1, group_chat_id2)))
async def handle_new_message(event):
    # Check if the message is from one of the two specific users
    from_id = str(event.message.from_id)
    str_event_chat_id = str(event.chat_id)
    if user1_id in (from_id) or user2_id in (from_id):
        # Copy the message text and URL
        message_text = event.message.message
        message_url = f"https://t.me/c/{str_event_chat_id[4:]}/{event.message.id}"

        # Download the media if any
        media_entity = None
        if event.message.media:
            progress_callback = lambda current, total: print(
                "Downloaded", current, "out of", total, "bytes"
            )
            media_entity = await event.message.download_media(
                progress_callback=progress_callback
            )

        # Check if this is a reply message
        if event.message.reply_to_msg_id:
            # Find the original message using its ID
            original_message = await event.get_reply_message()
            original_text = original_message.text
            original_url = f"https://t.me/c/{str_event_chat_id[4:]}/{event.chat_id}/{original_message.id}"

            # Send both messages to yourself
            sent_message = await new_client.send_message(
                original_number,
                f"ORIGINAL MESSAGE\n{original_text}\n{original_url}\n\nREPLY MESSAGE\n{message_text}\n{message_url}",
            )
            if media_entity:
                await new_client.send_file(
                    original_number, media_entity, caption=sent_message.text
                )

        else:
            # Send only the current message to yourself
            sent_message = await new_client.send_message(
                original_number, f"{message_text}\n{message_url}"
            )
            if media_entity:
                await new_client.send_file(
                    original_number, media_entity, caption=sent_message.text
                )


# Start the client and run it until interrupted
with original_client:
    original_client.run_until_disconnected()

with new_client:
    new_client.run_until_disconnected()
