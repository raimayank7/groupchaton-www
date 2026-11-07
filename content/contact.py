"""Content for /p/contact-us.html"""

TITLE = "Contact Us – GroupChatOn"
DESC  = ("Get in touch with the GroupChatOn team — report issues, "
         "ask questions, or suggest a tool.")
CANONICAL   = "/p/contact-us.html"
OMIT_FOOTER = "contact"
EXTRA_CSS   = """\
.wrap{max-width:640px}
.sub{color:var(--tx2);margin-bottom:40px;font-size:.95rem}
.card{background:var(--sf);border:1px solid var(--bd);border-radius:var(--r);padding:28px 32px;margin-bottom:24px}
h2{font-size:1rem;font-weight:700;margin-bottom:14px}
label{display:block;font-size:.85rem;font-weight:600;color:var(--tx2);margin-bottom:5px}
input,select,textarea{
  width:100%;padding:10px 13px;border-radius:7px;
  border:1px solid var(--bd);background:var(--bg);
  color:var(--tx);font-family:var(--sans);font-size:.9rem;
  outline:none;transition:border-color .15s;margin-bottom:16px;
}
input:focus,select:focus,textarea:focus{border-color:var(--gco)}
textarea{min-height:120px;resize:vertical}
.btn{
  display:inline-flex;align-items:center;gap:8px;
  background:var(--gco);color:#fff;border:none;cursor:pointer;
  padding:12px 24px;border-radius:8px;font-weight:700;
  font-family:var(--sans);font-size:.9rem;
  transition:background .15s,transform .15s;
}
.btn:hover{background:var(--gco-dk);transform:translateY(-1px)}
.btn:disabled{opacity:.6;cursor:not-allowed;transform:none}
.note{font-size:.82rem;color:var(--tx2);margin-top:8px}
.topics{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
.topic{
  padding:6px 14px;border-radius:20px;font-size:.82rem;font-weight:600;
  background:transparent;border:1.5px solid var(--bd);color:var(--tx2);
  cursor:pointer;transition:border-color .15s,color .15s,background .15s;
}
.topic:hover,.topic.on{border-color:var(--gco);color:var(--gco);background:rgba(95,179,76,.08)}
#result{display:none;padding:14px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:12px}
#result.ok{background:rgba(95,179,76,.12);color:var(--gco)}
#result.err{background:rgba(220,38,38,.1);color:#ef4444}
/* clip honeypot off-screen without absolute positioning (avoids RTL scroll) */
.hny{clip:rect(0,0,0,0);position:absolute;width:1px;height:1px;overflow:hidden}"""

BODY = """\
<div class="wrap">
  <h1>Contact Us</h1>
  <p class="sub">Found a bug, have a question, or want to suggest a tool? We’d love to hear from you.</p>

  <div class="card">
    <h2>What is this about?</h2>
    <div class="topics" id="topics" role="group" aria-label="Topic">
      <button type="button" class="topic" data-t="Bug or error">Bug or error</button>
      <button type="button" class="topic" data-t="Suggest a tool">Suggest a tool</button>
      <button type="button" class="topic" data-t="Infinity Tools">Infinity Tools</button>
      <button type="button" class="topic" data-t="Share groups">Share groups</button>
      <button type="button" class="topic" data-t="Help articles">Help articles</button>
      <button type="button" class="topic" data-t="Toolkit">Toolkit</button>
      <button type="button" class="topic" data-t="Send">Send</button>
      <button type="button" class="topic" data-t="Novels App">Novels App</button>
      <button type="button" class="topic" data-t="Sponsor / advertise">Sponsor / advertise</button>
      <button type="button" class="topic" data-t="Other">Other</button>
    </div>

    <form id="cf" novalidate>
      <span class="hny" aria-hidden="true"><input tabindex="-1" autocomplete="off" name="_gotcha"></span>
      <input type="hidden" name="_subject" id="cf-subject" value="GroupChatOn Contact">
      <input type="hidden" name="_next" value="https://www.groupchaton.com/p/contact-us.html?sent=1">
      <label for="cf-msg">Your message <span style="color:#ef4444">*</span></label>
      <textarea id="cf-msg" name="message" placeholder="Describe what you found or what you need…" required></textarea>
      <label for="cf-name">Your name (optional)</label>
      <input id="cf-name" name="name" type="text" placeholder="e.g. Priya" autocomplete="name">
      <label for="cf-reply">Email or phone to reply to (optional)</label>
      <input id="cf-reply" name="email" type="text" placeholder="e.g. hello@example.com" autocomplete="email">
      <button type="submit" class="btn" id="cf-send">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
        Send message
      </button>
      <div id="result" role="status"></div>
    </form>
    <p class="note">We read every message. Expect a reply within 2–3 days if you left a contact.</p>
  </div>
</div>"""

SCRIPT = """\
<script>
(function(){
  var SUBMIT_URL = 'https://formsubmit.co/ajax/c0c4166b4b4ea6af3c9385ffa0f56633';

  var chosen = '';
  var btns = document.querySelectorAll('.topic');
  btns.forEach(function(b){
    b.addEventListener('click',function(){
      btns.forEach(function(x){x.classList.remove('on')});
      b.classList.add('on');
      chosen = b.getAttribute('data-t');
      document.getElementById('cf-subject').value =
        'GroupChatOn' + (chosen ? ' – ' + chosen : '');
    });
  });

  if(location.search.indexOf('sent=1') !== -1){
    var r = document.getElementById('result');
    r.textContent = '✓ Message sent! We\'ll reply within 2–3 days.';
    r.className = 'ok'; r.style.display = '';
  }

  var form = document.getElementById('cf');
  var result = document.getElementById('result');
  var t0 = Date.now();

  form.addEventListener('submit', function(ev){
    var msg   = document.getElementById('cf-msg').value.trim();
    var hny   = form.querySelector('[name="_gotcha"]').value;

    if(hny) return;
    if(Date.now() - t0 < 3000) return;
    if(msg.length < 10){
      ev.preventDefault();
      showResult('Please write a message of at least 10 characters.', false);
      return;
    }

    ev.preventDefault();
    var name  = document.getElementById('cf-name').value.trim();
    var reply = document.getElementById('cf-reply').value.trim();
    var btn   = document.getElementById('cf-send');
    btn.disabled = true;
    btn.textContent = 'Sending…';

    fetch(SUBMIT_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({
        message: msg,
        name: name || '(not given)',
        email: reply || '(not given)',
        _subject: document.getElementById('cf-subject').value,
        _captcha: 'false'
      })
    })
    .then(function(r){ return r.json(); })
    .then(function(d){
      if(d.success === 'true'){
        showResult('✓ Message sent! We\'ll reply within 2–3 days.', true);
        form.reset(); chosen = '';
        btns.forEach(function(x){ x.classList.remove('on'); });
        document.getElementById('cf-subject').value = 'GroupChatOn Contact';
      } else {
        showResult('Something went wrong. Try again or message us on WhatsApp.', false);
      }
    })
    .catch(function(){
      showResult('Could not send — check your connection and try again.', false);
    })
    .finally(function(){
      btn.disabled = false;
      btn.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg> Send message';
    });
  });

  function showResult(msg, ok){
    result.textContent = msg;
    result.className = ok ? 'ok' : 'err';
    result.style.display = '';
  }
})();
</script>"""
