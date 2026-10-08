from pathlib import Path
import re, html, json, shutil, zipfile, os
root=Path('/tmp/v24')
template=(root/'classplus-vs-platfer.html').read_text()
# extract shared body shell before page-content + footer onward
body_start=template.index('<body class="seo-page">')
pc_start=template.index('<div id="page-content">')
footer_start=template.index('<footer class="site-footer">')
prefix=template[:pc_start]
suffix=template[footer_start:]

pages={
'best-classplus-alternatives.html':{
'title':'Best Classplus Alternatives in India (2026) for Coaching Institutes & Teachers | Platfer',
'desc':'Looking for Classplus alternatives? Compare coaching platforms for branded apps, teaching, tests, attendance, fees, student discovery and coaching growth. See where Platfer fits for independent teachers and local coaching institutes.',
'eyebrow':'Classplus alternatives · India 2026',
'h1':'Best Classplus Alternatives in India for Coaching Institutes & Teachers',
'lead':'If you are comparing Classplus alternatives, the important question is not only “which app gives me a branded app?” It is “how will I teach, manage my coaching and help new students discover me?” This guide compares the main approaches and explains where Platfer is different.',
'sections':[
('What to compare before choosing a Classplus alternative','A coaching platform should be judged on the complete workflow: student discovery, teaching, batches, attendance, fees, tests, notes, communication, online learning and the cost of getting started. A branded app can be useful, but it does not automatically solve student acquisition.'),
('Why independent teachers look for alternatives','Teachers and small institutes often want a lower barrier to getting online, simple management tools and a way to reach students beyond people who already know the coaching name. Current comparison pages in India commonly frame the market around branded apps, course delivery, management and pricing models. citeturn0search0turn0search2'),
('Platfer vs the traditional branded-app approach','Platfer combines a coaching presence with teaching and management features. Instead of treating the app as only a private digital space for an existing audience, Platfer adds a discovery layer where students can find coaching options and then learn from them. That makes the value proposition especially relevant to local and independent coaching institutes.'),
('What Platfer gives a coaching institute','A coaching can create its presence, teach live, publish recorded lectures and notes, create tests, organise batches, manage attendance and fees, communicate with students and make its coaching discoverable to students in its city. The platform is designed so a teacher does not have to solve every part of the digital journey separately.'),
('Is Platfer the right Classplus alternative for everyone?','No platform is best for every institute. If your only requirement is a particular branded-app workflow, compare the exact current plan and contract terms directly with the provider. If your bigger problem is getting your local coaching online while also being discoverable to new students and managing day-to-day teaching, Platfer is built around that broader use case.'),
],
'faq':[('What is the best Classplus alternative in India?','The best option depends on the institute. Compare student discovery, teaching, management, pricing, commissions, branding and whether the platform helps you acquire new students. Platfer is differentiated by combining coaching discovery with teaching and management tools.'),('Is there a free Classplus alternative?','Platfer offers its core teacher/coaching platform as a free starting point. Features and commercial terms can change, so check the current product before making a business decision.'),('What should I check before switching from Classplus?','Check student and content migration, payment terms, commissions, app/website requirements, teaching tools, management tools and how students will discover your coaching after the switch.'),('Does a branded coaching app automatically bring students?','No. A branded app primarily gives an existing coaching audience a digital destination. Student acquisition and discovery are a separate problem.')]
},
'best-teachmint-alternatives.html':{
'title':'Best Teachmint Alternatives in India (2026) for Teachers & Coaching Institutes | Platfer',
'desc':'Compare Teachmint alternatives for online teaching, coaching management, live classes, tests, attendance, fees and student discovery in India. See where Platfer fits.',
'eyebrow':'Teachmint alternatives · India 2026',
'h1':'Best Teachmint Alternatives in India for Teachers & Coaching Institutes',
'lead':'Teachers comparing Teachmint alternatives usually have a specific problem to solve: teaching online, managing a coaching centre, selling learning, or reaching more students. This guide focuses on the complete coaching journey rather than only feature counts.',
'sections':[
('Start with the problem, not the app name','Teachmint and other education platforms can serve different use cases. Current 2026 comparison results show the market splitting between classroom/institution management, course selling, branded apps and coaching operations. citeturn0search1turn0search7'),
('Where Platfer is different','Platfer is built for the combination of coaching discovery + teaching + management. A local coaching can present its coaching to students, run online learning and use tools for batches, attendance, fees, tests, notes and communication.'),
('Teach online and still remain a local coaching','A local coaching does not have to choose between offline identity and online learning. Platfer lets the coaching keep its identity while using live and recorded learning workflows and making the coaching easier for students to discover.'),
('What to compare','Compare discovery, live classes, recorded lectures, tests, attendance, fees, batch management, student communication, branded presence, pricing and commission. Also check whether the platform is helping you acquire new students or only giving your existing students a digital classroom.'),
('When another platform may be a better fit','If you need a highly specialised school ERP, hardware-focused classroom system or a particular enterprise LMS workflow, evaluate those products on their own strengths. Platfer is primarily differentiated around coaching growth, discovery, teaching and everyday management.'),
],
'faq':[('What is the best Teachmint alternative for coaching institutes?','There is no universal winner. A coaching institute should compare teaching, management, student acquisition and total cost. Platfer is designed around the combined discovery + teaching + management workflow.'),('Can I teach online from home with Platfer?','Yes. Teachers can use online teaching workflows such as live classes and recorded learning, while also building a coaching presence for students.'),('Is Teachmint better for every teacher?','No. The right platform depends on whether the teacher needs school/classroom management, course selling, coaching management or student acquisition.')]
},
'how-to-teach-online-from-home-in-india.html':{
'title':'How to Teach Online from Home in India: Complete Guide for Teachers | Platfer',
'desc':'Learn how to teach online from home in India with a phone or laptop, live classes, recorded lectures, notes, tests, student communication and low-data workflows.',
'eyebrow':'Teacher guide · Online teaching',
'h1':'How to Teach Online from Home in India',
'lead':'You do not need a complicated studio to start teaching online. The practical setup is a reliable phone or laptop, stable internet, a simple teaching workflow and one place where students can find classes, notes, tests and updates.',
'sections':[
('1. Decide what you will teach online','Start with one subject, class or exam category. A focused first batch is easier to schedule, promote and support than trying to put your entire coaching online at once.'),
('2. Choose a simple teaching setup','A phone can be enough for many teachers. Use a tripod or stable stand, a quiet room, adequate light and a microphone/headset if your environment is noisy. For board teaching, use a physical whiteboard or a digital writing setup depending on your subject.'),
('3. Plan live + recorded learning','Use live classes for explanation, doubt solving and interaction. Use recorded lectures for revision and students who miss a class. Keep notes and tests alongside the lessons so students do not need to search through many WhatsApp messages.'),
('4. Manage batches, attendance and tests','As your students increase, track batches, attendance, fees, tests and communication systematically. A coaching platform can reduce the number of separate spreadsheets and chat groups needed for daily work.'),
('5. Make your coaching discoverable','This is the part many teachers miss. Students cannot join a coaching they do not know exists. A digital presence should help students discover the coaching by city, subject or learning need — not only after someone sends them the coaching name.'),
('6. Use Platfer for the full workflow','Platfer combines coaching presence, student discovery, live and recorded learning, notes, tests, batch workflows, attendance, fees and communication so an independent teacher can build an online teaching system without first building a separate technology stack.'),
('Low-data teaching tips','Keep video resolution reasonable, avoid unnecessary camera backgrounds and animations, share compressed notes, record shorter revision lessons and provide a fallback when a student cannot stay in a live session. For weak networks, prioritise audio clarity and lesson continuity over heavy visual effects.'),
],
'faq':[('Can I teach online from home using only a phone?','Yes. Many teaching workflows can start with a phone, stable internet, a quiet environment and a simple class plan. A laptop can be added later when you need more advanced preparation.'),('How do I get students for online teaching?','Use a clear subject/course offer, referrals, social channels, local discovery and a public coaching presence. A teaching platform alone does not guarantee student acquisition.'),('How can I teach online with low internet?','Reduce video quality when necessary, prioritise clear audio, keep materials lightweight and provide recordings or notes for students who lose connection.')]
},
'free-online-test-maker-for-teachers.html':{
'title':'Free Online Test Maker for Teachers & Coaching Institutes | Platfer',
'desc':'Create online tests for students with a simple free test-making workflow. Build practice tests for school classes, tuition batches and competitive-exam preparation with Platfer.',
'eyebrow':'Free teacher tool · Tests',
'h1':'Free Online Test Maker for Teachers',
'lead':'Teachers need a test quickly — not another complicated setup. Use a simple test workflow for school classes, tuition batches and competitive-exam practice, then keep tests connected to your teaching and student workflow.',
'sections':[
('Why teachers need an online test maker','Online tests make it easier to give practice work, check understanding and organise revision. For coaching institutes, tests also become part of the regular batch workflow instead of a separate activity.'),
('Create tests around your actual syllabus','Start with class, subject, chapter or exam. Add questions, options, correct answers and marks. Keep instructions short and make the test comfortable to complete on a mobile screen.'),
('Use tests with live and recorded classes','A good teaching workflow connects the lesson to practice: teach a concept, share notes, give a short test, review weak areas and then assign revision. This is more useful than publishing tests with no learning context.'),
('Keep the student experience simple','Students should be able to understand what the test is about, how much time they have and how marks are calculated. Avoid unnecessary screens and heavy media when a simple question is enough.'),
('Platfer for coaching tests','Platfer is built around a wider coaching workflow, so tests can sit alongside batches, live classes, recorded lectures, notes, attendance and student communication instead of being an isolated test website.'),
],
'faq':[('Is this online test maker free?','Platfer provides free tools and a free starting platform for teachers. Always check the current product for the latest feature availability.'),('Can coaching institutes use online tests?','Yes. Online tests are useful for tuition batches, school classes and competitive-exam preparation. The workflow can be combined with notes, classes and revision.'),('Can students take tests on mobile?','The website and learning experience are designed with mobile users in mind; keep tests concise and mobile-friendly.')]
},
'free-attendance-tracker-excel-template-for-tutors.html':{
'title':'Free Attendance Tracker Excel Template for Tutors & Coaching Classes | Platfer',
'desc':'Get a simple free attendance tracker template for tutors and coaching classes. Track student attendance by date, batch and student without complicated software.',
'eyebrow':'Free teacher tool · Attendance',
'h1':'Free Attendance Tracker Excel Template for Tutors',
'lead':'Still marking attendance in a notebook or scattered WhatsApp messages? Start with a simple attendance sheet that works for a tuition batch or coaching class, then move to digital attendance when your student count grows.',
'sections':[
('What an attendance tracker should contain','At minimum, keep student name, batch, date and attendance status. For a monthly sheet, add totals or attendance percentage so you can quickly see which students are missing classes.'),
('Simple Excel workflow','Create one row per student and one column per class/date. Use consistent values such as Present, Absent and Leave. Keep a separate sheet for each batch if your coaching has multiple schedules.'),
('Why a digital attendance system helps later','Excel is useful for starting small, but as batches grow, manual updates become repetitive. A coaching platform can connect attendance with student records, batches and communication so the same information does not have to be entered repeatedly.'),
('Download or use Platfer','Use a simple tracker when you need a lightweight sheet. If you want attendance connected with batches, students, fees and teaching workflows, Platfer provides a broader coaching-management environment.'),
],
'faq':[('Is there a free attendance tracker for tutors?','Yes. A simple spreadsheet can handle attendance for small batches. Platfer also provides coaching attendance workflows for institutes that need more than a standalone sheet.'),('Can I use the attendance tracker for multiple batches?','Yes. Keep separate sheets or tabs for different batches and use consistent student records.'),('When should I move from Excel to coaching software?','When you have multiple batches, frequent attendance updates, student communication needs or staff members entering records, a connected system can save time.')]
},
'how-to-stream-live-classes-on-low-internet-bandwidth.html':{
'title':'How to Stream Live Classes on Low Internet Bandwidth | Teacher Guide India | Platfer',
'desc':'Practical tips for teachers to conduct live online classes on slow or unstable internet in India, reduce data use and keep students learning when the connection drops.',
'eyebrow':'Teacher guide · Low bandwidth',
'h1':'How to Stream Live Classes on Low Internet Bandwidth',
'lead':'A weak connection should not automatically end a class. The goal is to reduce unnecessary data use, prioritise clear teaching and give students a fallback when the network becomes unstable.',
'sections':[
('Use audio-first thinking','If the network is struggling, clear audio and understandable teaching are more important than high-resolution video. Reduce camera quality when necessary and avoid heavy animated backgrounds.'),
('Keep teaching materials lightweight','Compress PDFs and images before sharing. Prefer a clean board, short slides and small files over large downloads. Give students notes before or after class so they are not dependent on a continuous video stream.'),
('Have a fallback plan','If the live connection breaks, keep a recording or lesson notes available. Tell students where the next update will appear so they do not repeatedly call or message the teacher for the same information.'),
('Reduce unnecessary background traffic','Close downloads, cloud-sync jobs and other high-bandwidth applications while teaching. If possible, use a stable Wi-Fi/mobile-data position with the strongest signal available.'),
('Build low-bandwidth resilience into the workflow','A good online teaching system should not assume perfect internet. Combining live classes with recordings, notes, tests and simple communication gives students another way to continue learning when the live stream is interrupted.'),
('Platfer for practical online teaching','Platfer brings live/recorded learning, notes, tests and coaching management together so teachers can keep the learning workflow organised even when connectivity is not perfect.'),
],
'faq':[('What is the best video quality for slow internet?','Use the lowest quality that still lets students understand the lesson clearly. Audio clarity and continuity are often more important than high-resolution video.'),('How can I teach online if students keep losing connection?','Provide recordings, notes and short revision materials so students can continue after reconnecting.'),('Should I use live classes or recorded lectures on slow internet?','Use both where possible: live classes for interaction and recordings for students who experience interruptions.')]
},
}

def schema_for(p,url):
    faq=p.get('faq',[])
    data={"@context":"https://schema.org","@type":"WebPage","name":p['title'],"description":p['desc'],"url":url,"isPartOf":{"@type":"WebSite","name":"Platfer","url":"https://platfer.in/"}}
    faqdata={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    return '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False,separators=(',',':'))+'</script>\n<script type="application/ld+json">'+json.dumps(faqdata,ensure_ascii=False,separators=(',',':'))+'</script>'

def main_html(p):
    cards=''.join(f'<article class="seo-card feature-card"><div class="mini">{i+1}</div><h3>{html.escape(h)}</h3><p>{txt}</p></article>' for i,(h,txt) in enumerate(p['sections'][:3]))
    rest=''.join(f'<section class="seo-section"><div class="wrap"><div class="seo-head"><div class="eyebrow">Practical guide</div><h2>{html.escape(h)}</h2><p>{txt}</p></div></div></section>' for h,txt in p['sections'][3:])
    faq=''.join(f'<details class="seo-card"><summary><strong>{html.escape(q)}</strong></summary><p>{html.escape(a)}</p></details>' for q,a in p.get('faq',[]))
    return f'''<div id="page-content"><main class="seo-main">
<section class="seo-hero"><div class="hero__canvas-wrap" id="heroCanvasWrap"></div><div class="hero__scrim"></div><div class="seo-hero-content">
<div class="eyebrow">{p['eyebrow']}</div><h1>{html.escape(p['h1'])}</h1><p class="lead hero-lead-highlight">{p['lead']}</p>
<div class="seo-cta"><a class="gplay-btn" href="https://play.google.com/store/apps/details?id=com.platfer.app" rel="noopener noreferrer" target="_blank"><span class="seo-play-icon"><svg aria-hidden="true" viewbox="0 0 512 512"><path d="M99 20 L376 256 L99 492 Q88 480 88 462 L88 50 Q88 32 99 20 Z" fill="#00D3FF"></path><path d="M99 20 L325 172 L233 256 Z" fill="#00F076"></path><path d="M99 492 L325 340 L233 256 Z" fill="#EF4444"></path><path d="M325 172 L424 233 Q444 245 444 256 Q444 267 424 279 L325 340 L233 256 Z" fill="#FFC107"></path></svg></span><span class="g-txt"><span class="big">Download Platfer App</span><span class="small">From Google Play</span></span></a></div>
</div></section>
<section class="seo-section"><div class="wrap"><div class="seo-head"><div class="eyebrow">Quick answer</div><h2>{html.escape(p['sections'][0][0])}</h2><p>{p['sections'][0][1]}</p></div><div class="seo-grid">{cards}</div></div></section>
{rest}
<section class="seo-section"><div class="wrap"><div class="seo-head"><div class="eyebrow">FAQs</div><h2>Common questions</h2></div><div class="seo-grid">{faq}</div></div></section>
<section class="seo-section"><div class="wrap"><div class="seo-card seo-cta-card"><h2>Want the full coaching workflow?</h2><p>Platfer brings coaching discovery, online teaching and everyday coaching-management tools together so teachers can focus more on teaching and growth.</p><a class="gplay-btn" href="https://play.google.com/store/apps/details?id=com.platfer.app" rel="noopener noreferrer" target="_blank"><span class="g-txt"><span class="big">Get Platfer</span><span class="small">Free starting platform for teachers</span></span></a></div></div></section>
</main></div>'''

for fn,p in pages.items():
    out=prefix
    # head metadata replace
    out=re.sub(r'<title>.*?</title>',f'<title>{html.escape(p["title"])}</title>',out,count=1,flags=re.S)
    out=re.sub(r'<meta content="[^"]*" name="description"/>',f'<meta content="{html.escape(p["desc"])}" name="description"/>',out,count=1)
    url='https://platfer.in/'+fn
    out=re.sub(r'<link href="https://platfer.in/[^"]*" rel="canonical"/>',f'<link href="{url}" rel="canonical"/>',out,count=1)
    out=re.sub(r'<link href="https://platfer.in/[^"]*" hreflang="en-in" rel="alternate"/>',f'<link href="{url}" hreflang="en-in" rel="alternate"/>',out,count=1)
    out=re.sub(r'<link href="https://platfer.in/[^"]*" hreflang="x-default" rel="alternate"/>',f'<link href="{url}" hreflang="x-default" rel="alternate"/>',out,count=1)
    out=re.sub(r'<meta content="[^"]*" property="og:title"/>',f'<meta content="{html.escape(p["title"])}" property="og:title"/>',out,count=1)
    out=re.sub(r'<meta content="[^"]*" property="og:description"/>',f'<meta content="{html.escape(p["desc"])}" property="og:description"/>',out,count=1)
    out=re.sub(r'<meta content="https://platfer.in/[^"]*" property="og:url"/>',f'<meta content="{url}" property="og:url"/>',out,count=1)
    out=re.sub(r'<meta content="[^"]*" name="twitter:title"/>',f'<meta content="{html.escape(p["title"])}" name="twitter:title"/>',out,count=1)
    out=re.sub(r'<meta content="[^"]*" name="twitter:description"/>',f'<meta content="{html.escape(p["desc"])}" name="twitter:description"/>',out,count=1)
    out += schema_for(p,url)+'\n'
    out += main_html(p)+'\n'+suffix
    (root/fn).write_text(out,encoding='utf-8')

# Add/update links to existing pages without changing their visual structure: contextual resource links near end of main.
links='''<section class="seo-section"><div class="wrap"><div class="seo-head"><div class="eyebrow">More teacher resources</div><h2>Explore Platfer guides and tools</h2><p><a href="best-classplus-alternatives.html">Best Classplus Alternatives</a> · <a href="best-teachmint-alternatives.html">Best Teachmint Alternatives</a> · <a href="how-to-teach-online-from-home-in-india.html">How to Teach Online from Home in India</a> · <a href="free-online-test-maker-for-teachers.html">Free Online Test Maker</a> · <a href="free-attendance-tracker-excel-template-for-tutors.html">Free Attendance Tracker Excel Template</a> · <a href="how-to-stream-live-classes-on-low-internet-bandwidth.html">Live Classes on Low Internet Bandwidth</a> · <a href="free-timetable-generator.html">Free Coaching Timetable Generator</a></p></div></div></section>'''
for fn in ['teachmint-vs-platfer.html','classplus-vs-platfer.html','free-tools.html','free-attendance-generator.html','free-timetable-generator.html','free-fee-receipt-generator.html','coaching-management-app.html','online-teaching-app.html']:
    p=root/fn
    s=p.read_text(encoding='utf-8')
    if 'best-classplus-alternatives.html' not in s:
        s=s.replace('</main></div>',links+'</main></div>',1)
        p.write_text(s,encoding='utf-8')

# update sitemap
sm=root/'sitemap.xml'; s=sm.read_text()
newfiles=list(pages.keys())
for fn in newfiles:
    if f'https://platfer.in/{fn}' not in s:
        s=s.replace('</urlset>',f'  <url><loc>https://platfer.in/{fn}</loc><lastmod>2026-10-08</lastmod></url>\n</urlset>')
sm.write_text(s)

# Update llms.txt with discoverable resource map if present
ll=root/'llms.txt'
if ll.exists():
    st=ll.read_text(errors='ignore')
    block='''\n\n## Teacher discovery resources\n- Best Classplus Alternatives: https://platfer.in/best-classplus-alternatives.html\n- Best Teachmint Alternatives: https://platfer.in/best-teachmint-alternatives.html\n- How to Teach Online from Home in India: https://platfer.in/how-to-teach-online-from-home-in-india.html\n- Free Online Test Maker for Teachers: https://platfer.in/free-online-test-maker-for-teachers.html\n- Free Attendance Tracker Excel Template for Tutors: https://platfer.in/free-attendance-tracker-excel-template-for-tutors.html\n- How to Stream Live Classes on Low Internet Bandwidth: https://platfer.in/how-to-stream-live-classes-on-low-internet-bandwidth.html\n'''
    if 'Teacher discovery resources' not in st:
        ll.write_text(st.rstrip()+block+'\n')

# sanity checks
print('created',len(pages),'pages')
for fn in pages:
 s=(root/fn).read_text()
 print(fn, 'logo=', 'nav__logo-img' in s, 'adsense=', 'ca-pub-7444471000677426' in s, 'canonical=', 'canonical' in s, 'faq=', 'FAQPage' in s)
