import json

# Expanded dataset adding Section 3 for the eastward migration across linguistic families
modules_data = [
    {
        "section": "Section 1: Romance Core & Cognates",
        "scenarios": [
            {
                "context": "Año 1450 — Mainz Data Distribution Network",
                "clues": [
                    {"lang": "Spanish", "text": "El artesano Johannes Gutenberg perfecciona la imprenta con tipos móviles metálicos."},
                    {"lang": "Italian", "text": "L'artigiano perfeziona la tipografia con caratteri mobili."}
                ],
                "question": "Decode the numerical and lexical roots to identify the historical event:",
                "options": [
                    {"text": "1350 — The invention of the mechanical calculator using binary punch cards.", "correct": False},
                    {"text": "1450 — The perfection of the printing press with movable metal type.", "correct": True},
                    {"text": "1550 — The widespread distribution of hand-copied manuscript scrolls.", "correct": False}
                ]
            },
            {
                "context": "Anno 1492 — Iberian / Mediterranean Navigational Logs",
                "clues": [
                    {"lang": "French", "text": "Une expédition maritime traverse l'océan Atlantique et atteint le Nouveau Monde."},
                    {"lang": "Spanish", "text": "Una flota cruza el océano bajo el patrocinio de los Reyes Católicos."}
                ],
                "question": "Decode the numeral roots and context clues for this expedition:",
                "options": [
                    {"text": "1412 — The initial charting of the West African coastline.", "correct": False},
                    {"text": "1482 — The discovery of the direct maritime route to India.", "correct": False},
                    {"text": "1492 — Christopher Columbus's first voyage reaching the Americas.", "correct": True}
                ]
            }
        ]
    },
    {
        "section": "Section 2: Numeral & Structural Scaling",
        "scenarios": [
            {
                "context": "Año 1789 — Parisian System Override",
                "clues": [
                    {"lang": "French", "text": "La prise de la Bastille marque le début de la transformation politique radicale."},
                    {"lang": "Spanish", "text": "El levantamiento popular desmantela structures del antiguo régimen."}
                ],
                "question": "Decode the historical milestone and century markers:",
                "options": [
                    {"text": "1689 — The signing of the constitutional declaration.", "correct": False},
                    {"text": "1789 — The storming of the Bastille and start of the revolution.", "correct": True},
                    {"text": "1889 — The industrial exposition and global telegraph network launch.", "correct": False}
                ]
            }
        ]
    },
    {
        "section": "Section 3: The Eastward Pivot (Mediterranean & RTL Roots)",
        "scenarios": [
            {
                "context": "Eastward Transition — Root & Pattern Mechanics",
                "clues": [
                    {"lang": "Concept", "text": "Shifting from Latin/Romance left-to-right syntax to Semitic Right-to-Left (RTL) root-and-pattern frameworks."},
                    {"lang": "Arabic (Transliterated)", "text": "Kitab / Kataba (Book / To write - tracing the triliteral root K-T-B)."}
                ],
                "question": "When scanning Right-to-Left (RTL) scripts like Arabic or Hebrew, what is the primary structural shift required by your visual and cognitive decoding engine?",
                "options": [
                    {"text": "Memorizing thousands of entirely independent whole-word ideograms without roots.", "correct": False},
                    {"text": "Parsing core consonantal root triads (like K-T-B) while scanning in reverse optical vectors.", "correct": True},
                    {"text": "Translating every word strictly back into English sub-vocalizations before processing grammar.", "correct": False}
                ]
            }
        ]
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chrono-Lingua: Operational Interface</title>
    <style>
        :root {{
            --bg-color: #090d16;
            --card-bg: #111827;
            --border-color: #1f2937;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.15);
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
            --success: #10b981;
            --error: #ef4444;
        }}
        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0; padding: 2rem;
            display: flex; justify-content: center; align-items: center;
            min-height: 100vh;
        }}
        .container {{
            width: 100%; max-width: 750px;
            background-color: var(--card-bg);
            border-radius: 16px; padding: 2.5rem;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 0 15px rgba(56, 189, 248, 0.05);
            border: 1px solid var(--border-color);
        }}
        header {{
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.2rem; margin-bottom: 1.5rem;
        }}
        h1 {{ font-size: 1.4rem; margin: 0; color: var(--accent); letter-spacing: 0.05em; text-transform: uppercase; }}
        .stats {{ font-size: 0.85rem; color: var(--text-muted); font-family: monospace; }}
        .section-banner {{
            font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em;
            color: var(--accent); background: var(--accent-glow); padding: 0.4rem 0.8rem;
            border-radius: 4px; display: inline-block; margin-bottom: 1rem; border: 1px solid rgba(56, 189, 248, 0.2);
        }}
        .clue-box {{
            background: rgba(17, 24, 39, 0.8);
            border-left: 3px solid var(--accent);
            padding: 1rem 1.2rem; margin-bottom: 1rem;
            border-radius: 0 8px 8px 0;
            border-top: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
        }}
        .clue-lang {{ font-size: 0.7rem; text-transform: uppercase; color: var(--text-muted); font-weight: bold; margin-bottom: 0.2rem; letter-spacing: 0.05em; }}
        .clue-text {{ font-size: 1.05rem; font-style: italic; color: #e5e7eb; }}
        .question-title {{ font-weight: 600; margin: 1.5rem 0 1rem 0; font-size: 1.05rem; color: #f9fafb; }}
        .options-grid {{ display: flex; flex-direction: column; gap: 0.75rem; }}
        button.option-btn {{
            background-color: rgba(31, 41, 55, 0.5);
            color: var(--text-main); border: 1px solid var(--border-color);
            padding: 1rem; text-align: left; border-radius: 8px; cursor: pointer; transition: all 0.2s ease;
            font-size: 0.95rem;
        }}
        button.option-btn:hover:not(:disabled) {{ background-color: var(--accent-glow); border-color: var(--accent); }}
        button.option-btn.correct {{ background-color: rgba(16, 185, 129, 0.15); border-color: var(--success); color: #6ee7b7; }}
        button.option-btn.incorrect {{ background-color: rgba(239, 68, 68, 0.15); border-color: var(--error); color: #fca5a5; }}
        .feedback-area {{ margin-top: 1.5rem; padding: 1rem; border-radius: 8px; display: none; font-size: 0.95rem; }}
        .feedback-area.show {{ display: block; }}
        .feedback-area.success {{ background: rgba(16, 185, 129, 0.1); border: 1px solid var(--success); color: #6ee7b7; }}
        .feedback-area.error {{ background: rgba(239, 68, 68, 0.1); border: 1px solid var(--error); color: #fca5a5; }}
        .telemetry {{ margin-top: 0.5rem; font-size: 0.8rem; color: var(--text-muted); font-family: monospace; }}
        #next-btn {{
            margin-top: 1.5rem; background-color: var(--accent); color: #090d16;
            border: none; padding: 0.75rem 1.5rem; font-weight: bold; border-radius: 6px;
            cursor: pointer; display: none; float: right; font-size: 0.9rem;
        }}
        #next-btn:hover {{ background-color: #0ea5e9; }}
    </style>
</head>
<body>
<div class="container">
    <header>
        <h1>Chrono-Lingua // Engine</h1>
        <div class="stats" id="stats-display">INITIALIZING...</div>
    </header>
    <div id="game-canvas"></div>
    <div id="feedback" class="feedback-area"></div>
    <button id="next-btn" onclick="nextStep()">Next Node &rarr;</button>
</div>

<script>
    const moduleData = {modules_json};
    
    let queue = [];
    moduleData.forEach(mod => {{
        mod.scenarios.forEach(scen => {{
            queue.push(Object.assign({{ section: mod.section }}, scen));
        }});
    }});

    let currentIdx = 0;
    let score = 0;
    let startTime = 0;

    function loadScenario() {{
        const data = queue[currentIdx];
        document.getElementById('stats-display').innerText = `NODE [${{currentIdx + 1}}/${{queue.length}}]`;
        
        let html = `<div class="section-banner">${{data.section}}</div>`;
        html += `<div style="font-size: 0.85rem; color: var(--accent); margin-bottom: 1rem; font-weight: bold;">// ${{data.context}}</div>`;
        
        data.clues.forEach(clue => {{
            html += `
                <div class="clue-box">
                    <div class="clue-lang">${{clue.lang}}</div>
                    <div class="clue-text">"${{clue.text}}"</div>
                </div>
            `;
        }});

        html += `<div class="question-title">${{data.question}}</div><div class="options-grid">`;
        data.options.forEach((opt, idx) => {{
            html += `<button class="option-btn" onclick="checkAnswer(${{idx}})">${{opt.text}}</button>`;
        }});
        html += `</div>`;

        document.getElementById('game-canvas').innerHTML = html;
        document.getElementById('feedback').className = 'feedback-area';
        document.getElementById('next-btn').style.display = 'none';
        
        startTime = performance.now();
    }}

    function checkAnswer(selectedIndex) {{
        const endTime = performance.now();
        const durationMs = Math.round(endTime - startTime);
        
        const data = queue[currentIdx];
        const buttons = document.querySelectorAll('.option-btn');
        const feedback = document.getElementById('feedback');

        buttons.forEach((btn, idx) => {{
            btn.disabled = true;
            if (data.options[idx].correct) {{
                btn.classList.add('correct');
            }} else if (idx === selectedIndex) {{
                btn.classList.add('incorrect');
            }}
        }});

        if (data.options[selectedIndex].correct) {{
            feedback.innerHTML = `<strong>Access Granted:</strong> Linguistic pattern decoded.<div class="telemetry">Processing Latency: ${{durationMs}} ms</div>`;
            feedback.className = "feedback-area show success";
            score++;
        }} else {{
            feedback.innerHTML = `<strong>Decoding Mismatch:</strong> Translation variance detected.<div class="telemetry">Processing Latency: ${{durationMs}} ms</div>`;
            feedback.className = "feedback-area show error";
        }}

        const nextBtn = document.getElementById('next-btn');
        if (currentIdx < queue.length - 1) {{
            nextBtn.innerText = "Next Node →";
        }} else {{
            nextBtn.innerText = "View Diagnostics →";
        }}
        nextBtn.style.display = "block";
    }}

    function nextStep() {{
        currentIdx++;
        if (currentIdx < queue.length) {{
            loadScenario();
        }} else {{
            showCompletion();
        }}
    }}

    function showCompletion() {{
        document.getElementById('stats-display').innerText = `DIAGNOSTIC COMPLETE`;
        document.getElementById('game-canvas').innerHTML = `
            <div style="text-align: center; padding: 2rem 0;">
                <h2 style="color: var(--accent); margin-top: 0;">Module Cycle Finished</h2>
                <p style="font-size: 1.1rem; color: var(--text-muted);">Successfully processed ${{score}} / ${{queue.length}} historical nodes.</p>
                <p style="margin-top: 1rem; font-size: 0.9rem; color: var(--success);">Cognitive translation pipeline operating efficiently.</p>
            </div>
        `;
        document.getElementById('feedback').className = 'feedback-area';
        document.getElementById('next-btn').style.display = 'none';
    }}

    loadScenario();
</script>
</body>
</html>
"""

final_html = html_template.format(modules_json=json.dumps(modules_data, indent=4))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("[SUCCESS] Eastward expansion built: RTL transition nodes compiled.")import json

# Expanded dataset adding Section 3 for the eastward migration across linguistic families
modules_data = [
    {
        "section": "Section 1: Romance Core & Cognates",
        "scenarios": [
            {
                "context": "Año 1450 — Mainz Data Distribution Network",
                "clues": [
                    {"lang": "Spanish", "text": "El artesano Johannes Gutenberg perfecciona la imprenta con tipos móviles metálicos."},
                    {"lang": "Italian", "text": "L'artigiano perfeziona la tipografia con caratteri mobili."}
                ],
                "question": "Decode the numerical and lexical roots to identify the historical event:",
                "options": [
                    {"text": "1350 — The invention of the mechanical calculator using binary punch cards.", "correct": False},
                    {"text": "1450 — The perfection of the printing press with movable metal type.", "correct": True},
                    {"text": "1550 — The widespread distribution of hand-copied manuscript scrolls.", "correct": False}
                ]
            },
            {
                "context": "Anno 1492 — Iberian / Mediterranean Navigational Logs",
                "clues": [
                    {"lang": "French", "text": "Une expédition maritime traverse l'océan Atlantique et atteint le Nouveau Monde."},
                    {"lang": "Spanish", "text": "Una flota cruza el océano bajo el patrocinio de los Reyes Católicos."}
                ],
                "question": "Decode the numeral roots and context clues for this expedition:",
                "options": [
                    {"text": "1412 — The initial charting of the West African coastline.", "correct": False},
                    {"text": "1482 — The discovery of the direct maritime route to India.", "correct": False},
                    {"text": "1492 — Christopher Columbus's first voyage reaching the Americas.", "correct": True}
                ]
            }
        ]
    },
    {
        "section": "Section 2: Numeral & Structural Scaling",
        "scenarios": [
            {
                "context": "Año 1789 — Parisian System Override",
                "clues": [
                    {"lang": "French", "text": "La prise de la Bastille marque le début de la transformation politique radicale."},
                    {"lang": "Spanish", "text": "El levantamiento popular desmantela structures del antiguo régimen."}
                ],
                "question": "Decode the historical milestone and century markers:",
                "options": [
                    {"text": "1689 — The signing of the constitutional declaration.", "correct": False},
                    {"text": "1789 — The storming of the Bastille and start of the revolution.", "correct": True},
                    {"text": "1889 — The industrial exposition and global telegraph network launch.", "correct": False}
                ]
            }
        ]
    },
    {
        "section": "Section 3: The Eastward Pivot (Mediterranean & RTL Roots)",
        "scenarios": [
            {
                "context": "Eastward Transition — Root & Pattern Mechanics",
                "clues": [
                    {"lang": "Concept", "text": "Shifting from Latin/Romance left-to-right syntax to Semitic Right-to-Left (RTL) root-and-pattern frameworks."},
                    {"lang": "Arabic (Transliterated)", "text": "Kitab / Kataba (Book / To write - tracing the triliteral root K-T-B)."}
                ],
                "question": "When scanning Right-to-Left (RTL) scripts like Arabic or Hebrew, what is the primary structural shift required by your visual and cognitive decoding engine?",
                "options": [
                    {"text": "Memorizing thousands of entirely independent whole-word ideograms without roots.", "correct": False},
                    {"text": "Parsing core consonantal root triads (like K-T-B) while scanning in reverse optical vectors.", "correct": True},
                    {"text": "Translating every word strictly back into English sub-vocalizations before processing grammar.", "correct": False}
                ]
            }
        ]
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chrono-Lingua: Operational Interface</title>
    <style>
        :root {{
            --bg-color: #090d16;
            --card-bg: #111827;
            --border-color: #1f2937;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.15);
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
            --success: #10b981;
            --error: #ef4444;
        }}
        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0; padding: 2rem;
            display: flex; justify-content: center; align-items: center;
            min-height: 100vh;
        }}
        .container {{
            width: 100%; max-width: 750px;
            background-color: var(--card-bg);
            border-radius: 16px; padding: 2.5rem;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 0 15px rgba(56, 189, 248, 0.05);
            border: 1px solid var(--border-color);
        }}
        header {{
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.2rem; margin-bottom: 1.5rem;
        }}
        h1 {{ font-size: 1.4rem; margin: 0; color: var(--accent); letter-spacing: 0.05em; text-transform: uppercase; }}
        .stats {{ font-size: 0.85rem; color: var(--text-muted); font-family: monospace; }}
        .section-banner {{
            font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em;
            color: var(--accent); background: var(--accent-glow); padding: 0.4rem 0.8rem;
            border-radius: 4px; display: inline-block; margin-bottom: 1rem; border: 1px solid rgba(56, 189, 248, 0.2);
        }}
        .clue-box {{
            background: rgba(17, 24, 39, 0.8);
            border-left: 3px solid var(--accent);
            padding: 1rem 1.2rem; margin-bottom: 1rem;
            border-radius: 0 8px 8px 0;
            border-top: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
        }}
        .clue-lang {{ font-size: 0.7rem; text-transform: uppercase; color: var(--text-muted); font-weight: bold; margin-bottom: 0.2rem; letter-spacing: 0.05em; }}
        .clue-text {{ font-size: 1.05rem; font-style: italic; color: #e5e7eb; }}
        .question-title {{ font-weight: 600; margin: 1.5rem 0 1rem 0; font-size: 1.05rem; color: #f9fafb; }}
        .options-grid {{ display: flex; flex-direction: column; gap: 0.75rem; }}
        button.option-btn {{
            background-color: rgba(31, 41, 55, 0.5);
            color: var(--text-main); border: 1px solid var(--border-color);
            padding: 1rem; text-align: left; border-radius: 8px; cursor: pointer; transition: all 0.2s ease;
            font-size: 0.95rem;
        }}
        button.option-btn:hover:not(:disabled) {{ background-color: var(--accent-glow); border-color: var(--accent); }}
        button.option-btn.correct {{ background-color: rgba(16, 185, 129, 0.15); border-color: var(--success); color: #6ee7b7; }}
        button.option-btn.incorrect {{ background-color: rgba(239, 68, 68, 0.15); border-color: var(--error); color: #fca5a5; }}
        .feedback-area {{ margin-top: 1.5rem; padding: 1rem; border-radius: 8px; display: none; font-size: 0.95rem; }}
        .feedback-area.show {{ display: block; }}
        .feedback-area.success {{ background: rgba(16, 185, 129, 0.1); border: 1px solid var(--success); color: #6ee7b7; }}
        .feedback-area.error {{ background: rgba(239, 68, 68, 0.1); border: 1px solid var(--error); color: #fca5a5; }}
        .telemetry {{ margin-top: 0.5rem; font-size: 0.8rem; color: var(--text-muted); font-family: monospace; }}
        #next-btn {{
            margin-top: 1.5rem; background-color: var(--accent); color: #090d16;
            border: none; padding: 0.75rem 1.5rem; font-weight: bold; border-radius: 6px;
            cursor: pointer; display: none; float: right; font-size: 0.9rem;
        }}
        #next-btn:hover {{ background-color: #0ea5e9; }}
    </style>
</head>
<body>
<div class="container">
    <header>
        <h1>Chrono-Lingua // Engine</h1>
        <div class="stats" id="stats-display">INITIALIZING...</div>
    </header>
    <div id="game-canvas"></div>
    <div id="feedback" class="feedback-area"></div>
    <button id="next-btn" onclick="nextStep()">Next Node &rarr;</button>
</div>

<script>
    const moduleData = {modules_json};
    
    let queue = [];
    moduleData.forEach(mod => {{
        mod.scenarios.forEach(scen => {{
            queue.push(Object.assign({{ section: mod.section }}, scen));
        }});
    }});

    let currentIdx = 0;
    let score = 0;
    let startTime = 0;

    function loadScenario() {{
        const data = queue[currentIdx];
        document.getElementById('stats-display').innerText = `NODE [${{currentIdx + 1}}/${{queue.length}}]`;
        
        let html = `<div class="section-banner">${{data.section}}</div>`;
        html += `<div style="font-size: 0.85rem; color: var(--accent); margin-bottom: 1rem; font-weight: bold;">// ${{data.context}}</div>`;
        
        data.clues.forEach(clue => {{
            html += `
                <div class="clue-box">
                    <div class="clue-lang">${{clue.lang}}</div>
                    <div class="clue-text">"${{clue.text}}"</div>
                </div>
            `;
        }});

        html += `<div class="question-title">${{data.question}}</div><div class="options-grid">`;
        data.options.forEach((opt, idx) => {{
            html += `<button class="option-btn" onclick="checkAnswer(${{idx}})">${{opt.text}}</button>`;
        }});
        html += `</div>`;

        document.getElementById('game-canvas').innerHTML = html;
        document.getElementById('feedback').className = 'feedback-area';
        document.getElementById('next-btn').style.display = 'none';
        
        startTime = performance.now();
    }}

    function checkAnswer(selectedIndex) {{
        const endTime = performance.now();
        const durationMs = Math.round(endTime - startTime);
        
        const data = queue[currentIdx];
        const buttons = document.querySelectorAll('.option-btn');
        const feedback = document.getElementById('feedback');

        buttons.forEach((btn, idx) => {{
            btn.disabled = true;
            if (data.options[idx].correct) {{
                btn.classList.add('correct');
            }} else if (idx === selectedIndex) {{
                btn.classList.add('incorrect');
            }}
        }});

        if (data.options[selectedIndex].correct) {{
            feedback.innerHTML = `<strong>Access Granted:</strong> Linguistic pattern decoded.<div class="telemetry">Processing Latency: ${{durationMs}} ms</div>`;
            feedback.className = "feedback-area show success";
            score++;
        }} else {{
            feedback.innerHTML = `<strong>Decoding Mismatch:</strong> Translation variance detected.<div class="telemetry">Processing Latency: ${{durationMs}} ms</div>`;
            feedback.className = "feedback-area show error";
        }}

        const nextBtn = document.getElementById('next-btn');
        if (currentIdx < queue.length - 1) {{
            nextBtn.innerText = "Next Node →";
        }} else {{
            nextBtn.innerText = "View Diagnostics →";
        }}
        nextBtn.style.display = "block";
    }}

    function nextStep() {{
        currentIdx++;
        if (currentIdx < queue.length) {{
            loadScenario();
        }} else {{
            showCompletion();
        }}
    }}

    function showCompletion() {{
        document.getElementById('stats-display').innerText = `DIAGNOSTIC COMPLETE`;
        document.getElementById('game-canvas').innerHTML = `
            <div style="text-align: center; padding: 2rem 0;">
                <h2 style="color: var(--accent); margin-top: 0;">Module Cycle Finished</h2>
                <p style="font-size: 1.1rem; color: var(--text-muted);">Successfully processed ${{score}} / ${{queue.length}} historical nodes.</p>
                <p style="margin-top: 1rem; font-size: 0.9rem; color: var(--success);">Cognitive translation pipeline operating efficiently.</p>
            </div>
        `;
        document.getElementById('feedback').className = 'feedback-area';
        document.getElementById('next-btn').style.display = 'none';
    }}

    loadScenario();
</script>
</body>
</html>
"""

final_html = html_template.format(modules_json=json.dumps(modules_data, indent=4))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("[SUCCESS] Eastward expansion built: RTL transition nodes compiled.")





