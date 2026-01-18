from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

def count_vowels(text):
    return sum(1 for c in text.lower() if c in 'aeiou')

def count_consonants(text):
    return sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')

def alternate_case(text):
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text))

def leetspeak(text):
    leet_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    return ''.join(leet_map.get(c.lower(), c) for c in text.upper())

def get_fun_fact(name):
    facts = [
        f"If you say '{name}' backwards, it becomes '{name[::-1]}'! 🔄",
        f"Your name has {len(name)} letters - that's {len(name) * 10}% awesome! 🌟",
        f"The name '{name}' contains {count_vowels(name)} musical vowels! 🎵",
        f"Scientists estimate there are {random.randint(100, 9999)} people with your name! 👥",
        f"Your name's vibration frequency is {random.randint(100, 999)} Hz! (We made that up 😄)",
        f"Your name would look great on a billboard! 📢",
        f"In space, your name would sound the same! 🚀"
    ]
    return random.choice(facts)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dynamic Name Transformer 🎭</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
                overflow-x: hidden;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            .header {
                text-align: center;
                color: white;
                margin-bottom: 30px;
                animation: fadeInDown 0.8s ease-out;
            }
            .header h1 {
                font-size: 3em;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            @keyframes fadeInDown {
                from { opacity: 0; transform: translateY(-50px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .input-section {
                background: white;
                border-radius: 20px;
                padding: 30px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                margin-bottom: 30px;
                animation: slideInUp 0.8s ease-out;
            }
            @keyframes slideInUp {
                from { opacity: 0; transform: translateY(50px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .input-group {
                display: flex;
                gap: 10px;
                margin-bottom: 20px;
            }
            input[type="text"] {
                flex: 1;
                padding: 15px 20px;
                font-size: 1.2em;
                border: 2px solid #667eea;
                border-radius: 10px;
                outline: none;
                transition: all 0.3s;
            }
            input[type="text"]:focus {
                border-color: #764ba2;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
                transform: scale(1.02);
            }
            button {
                padding: 15px 30px;
                font-size: 1.2em;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.3s;
                font-weight: bold;
            }
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            }
            button:active {
                transform: translateY(0);
            }
            .transform-buttons {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 10px;
                margin-top: 15px;
            }
            .transform-btn {
                padding: 10px;
                font-size: 0.9em;
                background: #f8f9fa;
                color: #667eea;
                border: 2px solid #667eea;
            }
            .transform-btn:hover {
                background: #667eea;
                color: white;
            }
            .result-section {
                display: none;
                animation: bounceIn 0.6s ease-out;
            }
            @keyframes bounceIn {
                0% { opacity: 0; transform: scale(0.3); }
                50% { transform: scale(1.05); }
                100% { opacity: 1; transform: scale(1); }
            }
            .result-card {
                background: white;
                border-radius: 20px;
                padding: 30px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                margin-bottom: 20px;
            }
            .main-result {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px;
                border-radius: 15px;
                text-align: center;
                font-size: 2.5em;
                font-weight: bold;
                letter-spacing: 5px;
                margin-bottom: 20px;
                animation: pulse 2s ease-in-out infinite;
                word-wrap: break-word;
            }
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.02); }
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin: 20px 0;
            }
            .stat-box {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                transition: all 0.3s;
                border-left: 4px solid #667eea;
            }
            .stat-box:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            }
            .stat-number {
                font-size: 2em;
                font-weight: bold;
                color: #667eea;
                display: block;
            }
            .stat-label {
                color: #666;
                margin-top: 5px;
            }
            .variation-item {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                margin: 10px 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: all 0.3s;
            }
            .variation-item:hover {
                background: #e9ecef;
                transform: translateX(5px);
            }
            .fun-fact-box {
                background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                margin: 20px 0;
                font-size: 1.1em;
                animation: wiggle 3s ease-in-out infinite;
            }
            @keyframes wiggle {
                0%, 100% { transform: rotate(0deg); }
                25% { transform: rotate(1deg); }
                75% { transform: rotate(-1deg); }
            }
            .loading {
                display: none;
                text-align: center;
                padding: 20px;
            }
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #667eea;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                animation: spin 1s linear infinite;
                margin: 0 auto;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            h3 {
                color: #764ba2;
                margin-bottom: 15px;
                font-size: 1.5em;
            }
            .copy-btn {
                padding: 5px 15px;
                font-size: 0.9em;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .copy-btn:hover {
                background: #764ba2;
            }
            .floating {
                animation: float 3s ease-in-out infinite;
            }
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header floating">
                <h1>🎭 Dynamic Name Transformer</h1>
                <p>Type your name and watch the magic happen!</p>
            </div>

            <div class="input-section">
                <div class="input-group">
                    <input type="text" id="nameInput" placeholder="Enter your name..." autocomplete="off">
                    <button onclick="transformName()">✨ Transform</button>
                </div>
                
                <div class="transform-buttons">
                    <button class="transform-btn" onclick="quickTransform('upper')">UPPERCASE</button>
                    <button class="transform-btn" onclick="quickTransform('lower')">lowercase</button>
                    <button class="transform-btn" onclick="quickTransform('title')">Title Case</button>
                    <button class="transform-btn" onclick="quickTransform('alternate')">AlTeRnAtE</button>
                    <button class="transform-btn" onclick="quickTransform('reverse')">esreveR</button>
                    <button class="transform-btn" onclick="quickTransform('leet')">L33t Sp34k</button>
                </div>
            </div>

            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Transforming...</p>
            </div>

            <div class="result-section" id="resultSection">
                <div class="result-card">
                    <div class="main-result" id="mainResult"></div>
                    
                    <h3>📊 Live Statistics</h3>
                    <div class="stats-grid">
                        <div class="stat-box">
                            <span class="stat-number" id="lengthStat">0</span>
                            <span class="stat-label">Characters</span>
                        </div>
                        <div class="stat-box">
                            <span class="stat-number" id="vowelStat">0</span>
                            <span class="stat-label">Vowels</span>
                        </div>
                        <div class="stat-box">
                            <span class="stat-number" id="consonantStat">0</span>
                            <span class="stat-label">Consonants</span>
                        </div>
                        <div class="stat-box">
                            <span class="stat-number" id="wordsStat">1</span>
                            <span class="stat-label">Words</span>
                        </div>
                    </div>

                    <h3>🎨 Name Variations</h3>
                    <div id="variations"></div>

                    <div class="fun-fact-box" id="funFact">
                        💡 Click transform to see a fun fact!
                    </div>
                </div>
            </div>
        </div>

        <script>
            const nameInput = document.getElementById('nameInput');
            const resultSection = document.getElementById('resultSection');
            const loading = document.getElementById('loading');

            // Real-time input transformation
            nameInput.addEventListener('input', function() {
                if (this.value.trim()) {
                    quickUpdate();
                } else {
                    resultSection.style.display = 'none';
                }
            });

            // Enter key support
            nameInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    transformName();
                }
            });

            function quickUpdate() {
                const name = nameInput.value.trim();
                if (!name) return;

                resultSection.style.display = 'block';
                document.getElementById('mainResult').textContent = name.toUpperCase();
                
                // Update stats
                document.getElementById('lengthStat').textContent = name.length;
                document.getElementById('vowelStat').textContent = countVowels(name);
                document.getElementById('consonantStat').textContent = countConsonants(name);
                document.getElementById('wordsStat').textContent = name.split(/\s+/).filter(w => w).length;
            }

            async function transformName() {
                const name = nameInput.value.trim();
                if (!name) {
                    alert('Please enter a name!');
                    return;
                }

                loading.style.display = 'block';
                resultSection.style.display = 'none';

                try {
                    const response = await fetch(`/api/transform?name=${encodeURIComponent(name)}`);
                    const data = await response.json();

                    loading.style.display = 'none';
                    resultSection.style.display = 'block';

                    document.getElementById('mainResult').textContent = data.uppercase;
                    document.getElementById('lengthStat').textContent = data.length;
                    document.getElementById('vowelStat').textContent = data.vowels;
                    document.getElementById('consonantStat').textContent = data.consonants;
                    document.getElementById('wordsStat').textContent = name.split(/\s+/).filter(w => w).length;

                    // Display variations
                    const variations = document.getElementById('variations');
                    variations.innerHTML = `
                        <div class="variation-item">
                            <span><strong>Title Case:</strong> ${data.titlecase}</span>
                            <button class="copy-btn" onclick="copyText('${data.titlecase}')">Copy</button>
                        </div>
                        <div class="variation-item">
                            <span><strong>Lowercase:</strong> ${data.lowercase}</span>
                            <button class="copy-btn" onclick="copyText('${data.lowercase}')">Copy</button>
                        </div>
                        <div class="variation-item">
                            <span><strong>Reversed:</strong> ${data.reversed}</span>
                            <button class="copy-btn" onclick="copyText('${data.reversed}')">Copy</button>
                        </div>
                        <div class="variation-item">
                            <span><strong>L33t Speak:</strong> ${data.leetspeak}</span>
                            <button class="copy-btn" onclick="copyText('${data.leetspeak}')">Copy</button>
                        </div>
                    `;

                    // Get fun fact
                    const factResponse = await fetch(`/api/funfact?name=${encodeURIComponent(name)}`);
                    const factData = await factResponse.json();
                    document.getElementById('funFact').textContent = '💡 ' + factData.fact;

                } catch (error) {
                    loading.style.display = 'none';
                    alert('Error transforming name!');
                }
            }

            function quickTransform(type) {
                const name = nameInput.value.trim();
                if (!name) {
                    alert('Please enter a name first!');
                    return;
                }

                let result = '';
                switch(type) {
                    case 'upper': result = name.toUpperCase(); break;
                    case 'lower': result = name.toLowerCase(); break;
                    case 'title': result = name.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' '); break;
                    case 'alternate': result = name.split('').map((c, i) => i % 2 === 0 ? c.toUpperCase() : c.toLowerCase()).join(''); break;
                    case 'reverse': result = name.split('').reverse().join(''); break;
                    case 'leet': result = name.toUpperCase().replace(/A/g, '4').replace(/E/g, '3').replace(/I/g, '1').replace(/O/g, '0').replace(/S/g, '5').replace(/T/g, '7'); break;
                }

                resultSection.style.display = 'block';
                document.getElementById('mainResult').textContent = result;
                quickUpdate();
            }

            function countVowels(text) {
                return (text.match(/[aeiou]/gi) || []).length;
            }

            function countConsonants(text) {
                return (text.match(/[bcdfghjklmnpqrstvwxyz]/gi) || []).length;
            }

            function copyText(text) {
                navigator.clipboard.writeText(text).then(() => {
                    alert('Copied: ' + text);
                });
            }
        </script>
    </body>
    </html>
    """

@app.route('/api/transform')
def api_transform():
    name = request.args.get('name', '').strip()
    
    if not name:
        return jsonify({'error': 'Please provide a name parameter'}), 400
    
    return jsonify({
        'original': name,
        'uppercase': name.upper(),
        'lowercase': name.lower(),
        'titlecase': name.title(),
        'reversed': name[::-1],
        'length': len(name),
        'vowels': count_vowels(name),
        'consonants': count_consonants(name),
        'leetspeak': leetspeak(name)
    })

@app.route('/api/funfact')
def api_funfact():
    name = request.args.get('name', '').strip()
    if not name:
        return jsonify({'error': 'Please provide a name parameter'}), 400
    
    return jsonify({'fact': get_fun_fact(name)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)