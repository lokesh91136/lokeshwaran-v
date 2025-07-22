from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime
import json

app = Flask(__name__)

class WebsiteChatbot:
    def __init__(self):
        self.name = "WebBot"
        self.greetings = [
            "Hello! I'm WebBot, your website assistant. How can I help you today?",
            "Hi there! I'm here to help with your website questions. What would you like to know?",
            "Welcome! I'm WebBot, ready to assist with website-related queries."
        ]
        
        # Knowledge base for website-related questions
        try:
            with open('templates/data.json', 'r') as f:
                self.knowledge_base = json.load(f)
        except FileNotFoundError:
            # Fallback knowledge base if JSON file is not found
            self.knowledge_base = {
                'domain': {
                    'keywords': ['domain', 'domain name', 'url', 'website address'],
                    'responses': [
                        "A domain name is your website's address on the internet (e.g., www.yourwebsite.com). You can register domains through providers like GoDaddy, Namecheap, or Google Domains.",
                        "Domain names typically cost $10-15 per year. You'll need to renew them annually to keep your website accessible.",
                        "To register a domain, choose a domain registrar, check availability, and complete the registration process with your contact information."
                    ]
                },
                'hosting': {
                    'keywords': ['hosting', 'web hosting', 'server', 'host website'],
                    'responses': [
                        "Web hosting is a service that stores your website files on servers, making them accessible online. Popular hosting providers include Bluehost, HostGator, and SiteGround.",
                        "Shared hosting is the most affordable option ($3-10/month), while VPS and dedicated hosting offer more resources at higher costs.",
                        "When choosing hosting, consider factors like uptime, customer support, storage space, and bandwidth requirements."
                    ]
                },
                'design': {
                    'keywords': ['design', 'layout', 'look', 'appearance', 'theme', 'template'],
                    'responses': [
                        "Website design involves creating an attractive, user-friendly layout. You can use website builders like Wix, Squarespace, or WordPress with themes.",
                        "Good website design should be responsive (mobile-friendly), have clear navigation, and reflect your brand identity.",
                        "Consider hiring a professional designer or using pre-made templates to create a professional-looking website."
                    ]
                },
                'content': {
                    'keywords': ['content', 'text', 'images', 'videos', 'blog', 'pages'],
                    'responses': [
                        "Website content includes text, images, videos, and other media. Quality content should be relevant, engaging, and optimized for search engines.",
                        "Regular content updates help keep your website fresh and improve search engine rankings.",
                        "Consider creating a content calendar to plan regular updates and maintain consistency."
                    ]
                },
                'seo': {
                    'keywords': ['seo', 'search engine', 'google', 'ranking', 'traffic'],
                    'responses': [
                        "SEO (Search Engine Optimization) helps your website rank higher in search results. Key factors include quality content, fast loading speed, and mobile-friendliness.",
                        "To improve SEO, use relevant keywords, create quality content, optimize images, and build quality backlinks.",
                        "SEO is a long-term strategy that requires consistent effort and monitoring of your website's performance."
                    ]
                },
                'security': {
                    'keywords': ['security', 'ssl', 'https', 'secure', 'protection'],
                    'responses': [
                        "Website security is crucial. Always use HTTPS (SSL certificates) to encrypt data transmission between your site and visitors.",
                        "Keep your website software, plugins, and themes updated to protect against security vulnerabilities.",
                        "Consider implementing additional security measures like firewalls, regular backups, and malware scanning."
                    ]
                },
                'performance': {
                    'keywords': ['speed', 'performance', 'loading', 'fast', 'slow'],
                    'responses': [
                        "Website speed is important for user experience and SEO. Optimize images, use caching, and choose fast hosting to improve performance.",
                        "Tools like Google PageSpeed Insights can help you identify and fix performance issues on your website.",
                        "Aim for a loading time of under 3 seconds for optimal user experience."
                    ]
                },
                'maintenance': {
                    'keywords': ['maintenance', 'update', 'backup', 'monitor'],
                    'responses': [
                        "Regular website maintenance includes updating software, backing up data, monitoring performance, and checking for broken links.",
                        "Set up automated backups and consider using monitoring tools to track your website's uptime and performance.",
                        "Schedule regular maintenance tasks to keep your website running smoothly and securely."
                    ]
                }
            }
        
        self.fallback_responses = [
            "I'm not sure about that specific question, but I can help with general website topics like domains, hosting, design, SEO, security, and maintenance.",
            "That's an interesting question! While I don't have a specific answer, I can help you with common website-related topics.",
            "I'm still learning and don't have information about that yet. Try asking about domains, hosting, design, or other website basics!"
        ]

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check for greetings
        if any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
            return random.choice(self.greetings)
        
        # Check for thanks
        if any(word in user_input for word in ['thanks', 'thank you', 'appreciate']):
            return "You're welcome! I'm happy to help with your website questions."
        
        # Check for goodbye
        if any(word in user_input for word in ['bye', 'goodbye', 'see you', 'exit']):
            return "Goodbye! Feel free to return if you have more website questions. Have a great day!"
        
        # Check knowledge base
        for topic, data in self.knowledge_base.items():
            if any(keyword in user_input for keyword in data['keywords']):
                return random.choice(data['responses'])
        
        # Check for general website questions
        if any(word in user_input for word in ['website', 'site', 'web']):
            return "I can help you with various website topics including domains, hosting, design, content, SEO, security, performance, and maintenance. What specific area would you like to know more about?"
        
        # Fallback response
        return random.choice(self.fallback_responses)

# Initialize chatbot
chatbot = WebsiteChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message.strip():
        return jsonify({'response': 'Please enter a message.'})
    
    bot_response = chatbot.get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)



