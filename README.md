# telegram-group-chat-monitor-specific-user
To copy a message to myself if specific users in the specific group chats send out a message.


# to be ready
- register telegram API via https://core.telegram.org/api/obtaining_api_id
- pip install the library
- tested on Python 3.10.11


This code sets up an event handler for new messages in a group chat on Telegram and copies messages from specific users. It then downloads any media included in the message, checks if it is a reply message, and finds the original message using its ID. It sends both messages to another user's account or phone number with their own `api_id` and `api_hash`. The process repeats until interrupted. 

Here are some major steps that the code performs: 

- Import the required classes (`TelegramClient` and `events`) and libraries (`logging`). 
- Set up logging configuration using the `basicConfig()` method of the `logging` module. 
- Replace placeholders (`api_id`, `api_hash`, `group_chat_id1`, `group_chat_id2`, `original_number`, `new_number`, `user1_id`, and `user2_id`) with appropriate values. 
- Create two new instances of `TelegramClient` class with your API credentials – one for the current (original) session and another for the remote (new) session. 
- Define an event handler function named `handle_new_message` that takes an `event` parameter as input.
- Use the `NewMessage()` method of the `events` module to specify the parameters of new incoming messages such as group chats (`chats`), excluding forwarded messages (`forwarded`), and excluding edited messages (`edited`).
- Check if the message is from one of the two specific users (`user1_id` or `user2_id`). If yes, copy the message text and URL.
- Download the media if any and save it as `media_entity`.
- Check if this is a reply message. If so, find the original message using its ID and extract its details such as text and URL. Send both the original and reply messages to the target number or account. If there is any media content, send it as well.
- If it is not a reply message, send only the current message to the target number or account. If there is any media content, send it as well.
- Start both clients (current and remote sessions) using the `run_until_disconnected()` method of `TelegramClient` class and keep them running until interrupted.

Note: To run this code properly, one needs to replace all the placeholder values with their actual values.