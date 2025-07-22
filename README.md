# Website Chatbot - WebBot

A Python-based chatbot designed to answer questions about websites, domains, hosting, design, SEO, security, and more.

## Features

- 🤖 Intelligent responses to website-related questions
- 💬 Modern, responsive web interface
- 📱 Mobile-friendly design
- ⚡ Real-time chat experience
- 🎯 Quick suggestion buttons for common topics
- 🔄 Typing indicators for better UX

## Topics Covered

The chatbot can help with:
- **Domain Names**: Registration, costs, providers
- **Web Hosting**: Types, providers, selection criteria
- **Website Design**: Layout, themes, responsive design
- **Content Management**: Text, images, videos, blogs
- **SEO**: Search engine optimization strategies
- **Security**: SSL certificates, HTTPS, protection
- **Performance**: Speed optimization, loading times
- **Maintenance**: Updates, backups, monitoring

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and go to:**
   ```
   http://localhost:8080
   ```

## Usage

1. **Start a conversation** by typing your question in the chat input
2. **Use suggestion buttons** for quick access to common topics
3. **Ask about any website-related topic** and get helpful responses

## Example Questions

- "What is a domain name?"
- "Tell me about web hosting"
- "How to design a website?"
- "What is SEO?"
- "Website security tips"
- "How to improve website speed?"
- "Website maintenance tips"

## Project Structure

```
chatbot/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Chat interface
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Customization

### Adding New Topics

To add new topics to the chatbot, edit the `knowledge_base` in `app.py`:

```python
'new_topic': {
    'keywords': ['keyword1', 'keyword2'],
    'responses': [
        "Response 1",
        "Response 2",
        "Response 3"
    ]
}
```

### Modifying Responses

You can modify existing responses or add new ones by editing the `responses` arrays in the `knowledge_base`.

### Styling

The chat interface styling can be customized by modifying the CSS in `templates/index.html`.

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS with gradients and animations

## Requirements

- Python 3.7 or higher
- Flask 2.3.3
- Modern web browser

## License

This project is open source and available under the MIT License.

## Support

If you have any questions or need help with the chatbot, feel free to ask the bot itself or check the code comments for implementation details. 