from flask import Flask, request, jsonify

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>নারী ও শিশু আইন সহায়ক</title>
    <style>
        body{background:linear-gradient(135deg,#667eea,#764ba2);min-height:100vh;padding:20px;font-family:sans-serif}
        .card{max-width:800px;margin:auto;background:white;border-radius:25px;overflow:hidden}
        .header{background:linear-gradient(135deg,#1e3c72,#2b4c7c);color:white;padding:25px;text-align:center}
        .chat-area{height:400px;overflow-y:auto;padding:20px;background:#f8f9fa}
        .message{margin-bottom:15px;display:flex}
        .user{justify-content:flex-end}
        .ai{justify-content:flex-start}
        .bubble{max-width:70%;padding:10px 15px;border-radius:18px}
        .user .bubble{background:#1e3c72;color:white}
        .ai .bubble{background:white;border:1px solid #ddd}
        .input-area{padding:20px;background:white}
        .quick{background:#e9ecef;border:none;border-radius:20px;padding:8px 12px;margin:3px;cursor:pointer}
        .flex{display:flex;gap:10px;margin-top:10px}
        input{flex:1;padding:12px;border-radius:30px;border:2px solid #ddd}
        .btn{background:#1e3c72;color:white;border:none;border-radius:30px;padding:12px 20px;cursor:pointer}
        .footer{text-align:center;padding:12px;font-size:11px;color:#777}
    </style>
</head>
<body>
<div class="card">
    <div class="header"><h1>⚖️ নারী ও শিশু আইন সহায়ক</h1><p>থিসিস প্রজেক্ট 2026</p></div>
    <div id="chatBox" class="chat-area"><div class="text-center text-muted" style="margin-top:140px"><h4>💬 আপনার প্রশ্ন লিখুন</h4></div></div>
    <div class="input-area">
        <button class="quick" onclick="askq('যৌতুক দাবি করলে কী শাস্তি?')">📜 যৌতুক</button>
        <button class="quick" onclick="askq('শিশু আইন ২০১৩ কী বলে?')">👶 শিশু</button>
        <button class="quick" onclick="askq('ধর্ষণের শাস্তি কী?')">⚡ ধর্ষণ</button>
        <div class="flex"><input type="text" id="q"><button class="btn" onclick="send()">পাঠান</button></div>
    </div>
    <div class="footer"><p>© 2026 থিসিস প্রকল্প</p></div>
</div>
<script>
    const chat=document.getElementById('chatBox');
    function add(t,u){let d=document.createElement('div');d.className='message '+(u?'user':'ai');d.innerHTML='<div class="bubble">'+t+'</div>';chat.appendChild(d);chat.scrollTop=chat.scrollHeight;}
    async function send(){let q=document.getElementById('q').value.trim();if(!q)return;add(q,true);document.getElementById('q').value='';add('⏳ উত্তর লিখছি...',false);try{let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:q})});let d=await r.json();chat.lastChild.remove();add(d.answer,false);}catch(e){chat.lastChild.remove();add('সার্ভার সমস্যা',false);}}
    function askq(q){document.getElementById('q').value=q;send();}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

@app.route('/ask', methods=['POST'])
def ask():
    q = request.json.get('question', '')
    if 'যৌতুক' in q:
        ans = 'যৌতুক নিরোধ আইন, ২০১৮ এর ধারা ৪ অনুযায়ী যৌতুক দাবি করলে ৫-১০ বছর কারাদণ্ড।'
    elif 'শিশু' in q:
        ans = 'শিশু আইন, ২০১৩ এর ধারা ৪ অনুযায়ী ১৮ বছরের নিচে অপরাধ করলে কিশোর অপরাধী।'
    elif 'ধর্ষণ' in q:
        ans = 'নারী ও শিশু নির্যাতন দমন আইন, ২০০০ এর ধারা ৯ অনুযায়ী ধর্ষণের শাস্তি যাবজ্জীবন কারাদণ্ড।'
    else:
        ans = f'প্রশ্ন: "{q}"। আইন বিশেষজ্ঞের পরামর্শ নিন।'
    return jsonify({'answer': ans})

if __name__ == '__main__':
    app.run()
