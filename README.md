# Telegram-ChatGPT
A simple example of ChatGPT Telegram chatbot with command handlers

### Lets setup the environment

- open the command prompt.

- Ensure you have Python installed. 

### Create a virtual environment and activate it:

<!-- wp:code -->
<pre class="wp-block-code"><code lang="bash" class="language-bash">python -m venv chatbot-env
chatbot-env\Scripts\activate # On Windows
source chatbot-env/bin/activate # On Unix or MacOS</code></pre>
<!-- /wp:code -->

### Install the necessary packages:

<!-- wp:code -->
<pre class="wp-block-code"><code lang="bash" class="language-bash">pip install python-telegram-bot openai</code></pre>
<!-- /wp:code -->

### Get openAI API key

- Go to OpenAI's Platform website at platform.openai.com and sign in with an OpenAI account.

- Click your profile icon at the top-right corner of the page and select "View API Keys."

- Click "Create New Secret Key" to generate a new API key.

### Create a chatbot with BotFather

- You must have an account with telegram

- Find the BotFather: In the Telegram app, search for “BotFather.” This is a special bot provided by Telegram to help you create and manage other bots.

- Create a New Bot: Start a conversation with BotFather and follow the instructions to create a new bot. You will be prompted to provide a name and username for your bot. Once the process is complete, BotFather will provide you with an API key.

### Edit the preferences.conf

- update OPENAI_API_KEY, TELEGRAM_API_KEY and optionally edit the CharacterProfile and save.

### Run <!-- wp:code -->
<pre class="wp-block-code"><code class="">python main.py</code></pre>
<!-- /wp:code -->
