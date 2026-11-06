ABOUT_ME = (
    "I am Kübra Aktaş, 19 years old. My passion for software development, which began with a web design course at my vocational high school, pushed me to challenge my limits and build this visionary platform. When I stepped into the world of software, I wanted to dive deep, starting with foundational languages like Python. However, I found that the available resources were either overly complex, poorly organized, or limited to surface-level summaries. Defying the prejudice of those around me who said 'you cannot do it,' I decided to bring this comprehensive e-book and interactive learning ecosystem to life. My goal is to elevate every student starting from zero to a true level of engineering awareness. This project is my first signature in the technology world and the beginning of a much greater journey. As we build the future of technology together, I hope you will not withhold your support, and I wish for this guide to deeply inspire you."
)

COMMUNITY_CHANNELS = [
    {"name": "Instagram", "icon": "IG", "handle": "@codelucid_", "note": "Aesthetic Dev Content & Behind the Scenes", "href": "https://www.instagram.com/codelucid_/"},
    {"name": "TikTok", "icon": "TT", "handle": "@codelucid_", "note": "Quick Python Tips & Coding Snippets", "href": "https://www.tiktok.com/@codelucid_"},
    {"name": "GitHub", "icon": "GH", "handle": "://github.com_", "note": "Production Source Code Repositories", "href": "https://github.com_"},
    {"name": "LinkedIn", "icon": "IN", "handle": "Kubra Aktas", "note": "Aspiring Software Developer | Founder of codelucid_", "href": "https://www.linkedin.com/search/results/all/?keywords=Kubra%20Aktas"},
    {"name": "E-Mail", "icon": "@", "handle": "codelucid.contact@gmail.com", "note": "Official Support & Business Inquiries", "href": "mailto:codelucid.contact@gmail.com"}
]

ENGINEERING_MANIFESTO = (
    "This guide is structured not just to make you someone who writes code, but to transform you into a true engineer. "
    "The 'Modules & Package Management' and 'DSA (Data Structures & Algorithms)' sections are specifically crafted as an academic preparation. "
    "This is for readers who aim to step into the industry professionally or pursue majors like Software Engineering, Computer Science, Artificial Intelligence, or Computer Programming. "
    "Admittedly, the universe of data structures and algorithms is one of the longest, most challenging, and most intense phases in a developer's journey. "
    "The heart of computer science beats right here. The concepts you learn in these chapters form the core foundation of what you will encounter in university classrooms and international technical interviews. "
    "When you study these pages patiently and run every script on your computer, you will master not only Python but also how computers process data behind the scenes. "
    "Trust yourself on this challenging but deeply rewarding journey; you are ready to build the architecture of tomorrow!"
)

# Exhaustive Curriculum (Structure mapped per request)
CURRICULUM = [
    {
        "id": 1,
        "kicker": "Module 1",
        "title": "Python Fundamentals & Core Syntax",
        "summary": "A strategic orientation to Python as a professional engineering language, followed by a concise reference for the symbols that appear constantly in real Python programs.",
        "lessons": [
            {
                "heading": "The Core Symbols of Engineering",
                "body": "Memorize these foundational structural elements.",
                "code": "# Comments explain intent\nuser_active = True # Assignment\nif user_active == True: # Equality\n    permissions = ['read', 'write'] # Brackets for Lists\n    config = {'theme': 'dark'} # Braces for Dictionaries\n    print(config['theme']) # Parentheses for Execution"
            }
        ]
    },
    {
        "id": 2,
        "kicker": "Module 2",
        "title": "Basic Information & Conceptual Architecture",
        "summary": "How Python transforms source text into behavior in memory.",
        "lessons": []
    },
    # Modules 3 through 11 mapped here...
    {
        "id": 12,
        "kicker": "Module 12",
        "title": "Real-World Interactive Coding Blueprints",
        "summary": "Complete operational scripts combining syntax, algorithms, and application architecture.",
        "lessons": [
            {
                "heading": "Blueprint: Cyber Security Log Analyzer",
                "body": "Using Python to parse security logs and isolate failed authentication attempts dynamically.",
                "code": "logs = ['INFO: System start', 'ERROR: Auth fail IP 192.168.1.1', 'INFO: User login']\nfailed_ips = [log.split(' ')[-1] for log in logs if 'Auth fail' in log]\nprint('Isolated Threats:', failed_ips)"
            }
        ]
    }
]