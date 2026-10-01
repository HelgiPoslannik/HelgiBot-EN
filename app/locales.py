FREE_MESSAGE_LIMIT = 5
STARS_PACK_PRICE = 500
REQUESTS_PER_PACK = 20

MESSAGES = {
    "en": {
        "welcome": (
            "Hi there! 👋\n\n"
            "I help decode what your body (or your child's body) is trying to tell you "
            "through physical symptoms, diseases, and emotional triggers.\n\n"
            "💡 **Not sure how to start? Just send a message like:**\n"
            '• *"My 5-year-old child has constant eczema on their hands."*\n'
            '• *"I\'ve had lower back pain for 2 months, no injury."*\n'
            '• *"I feel total apathy and constant fatigue, even though my medical tests are normal."*\n\n'
            f"🎁 **You have {FREE_MESSAGE_LIMIT} FREE questions to start!**\n"
            f"*(Packages: {REQUESTS_PER_PACK} queries for {STARS_PACK_PRICE} ⭐️)*\n\n"
            "Describe your symptom or state below to begin:"
        ),
        "limit_reached": "You have run out of free and paid queries. Get a new pack to continue:",
        "invoice_title": f"{REQUESTS_PER_PACK} AI Assistant Queries",
        "invoice_desc": f"Pack of {REQUESTS_PER_PACK} additional queries for the AI Psychosomatics Assistant.",
        "invoice_label": f"{REQUESTS_PER_PACK} queries",
        "payment_success": f"Payment received! You’ve been credited with {REQUESTS_PER_PACK} queries. Feel free to continue 🙌"
    },
    "ru": {
        "welcome": (
            "Привет! 👋\n\n"
            "Я помогаю расшифровать, что твое тело (или тело твоего ребенка) пытается "
            "сказать через телесные симптомы, болезни и эмоциональные триггеры.\n\n"
            "💡 **Не знаешь, как начать? Просто отправь сообщение вроде:**\n"
            '• *"У моего 5-летнего ребенка постоянная экзема на руках."*\n'
            '• *"У меня уже 2 месяца болит поясница, хотя травм не было."*\n'
            '• *"Я чувствую полную апатию и упадок сил, хотя медицинские анализы в норме."*\n\n'
            f"🎁 **У тебя есть {FREE_MESSAGE_LIMIT} БЕСПЛАТНЫХ вопросов для старта!**\n"
            f"*(Пакеты: {REQUESTS_PER_PACK} запросов за {STARS_PACK_PRICE} ⭐️)*\n\n"
            "Опиши свой симптом или состояние ниже, чтобы начать:"
        ),
        "limit_reached": "Бесплатные и оплаченные запросы закончились. Вот пакет, чтобы продолжить:",
        "invoice_title": f"{REQUESTS_PER_PACK} запросов к ИИ-ассистенту",
        "invoice_desc": f"Пакет из {REQUESTS_PER_PACK} дополнительных запросов к ИИ-ассистенту по психосоматике.",
        "invoice_label": f"{REQUESTS_PER_PACK} запросов",
        "payment_success": f"Оплата получена! Начислено {REQUESTS_PER_PACK} запросов. Можешь продолжать 🙌"
    },
    "kk": {
        "welcome": (
            "Сәлем! 👋\n\n"
            "Мен денеңіздің (немесе балаңыздың денесінің) физикалық симптомдар, аурулар "
            "мен эмоционалды триггерлер арқылы не айтқысы келетінін түсінуге көмектесемін.\n\n"
            "💡 **Қалай бастауды білмейсіз бе? Осындай хабарлама жіберіңіз:**\n"
            '• *"5 жасар баламның қолында үнемі экзема бар."*\n'
            '• *"Жарақатсыз-ақ бел ауруына 2 ай болды."*\n'
            '• *"Медициналық анализдерім дұрыс болса да, бойымда әлсіздік пен апатия бар."*\n\n'
            f"🎁 **Бастау үшін сізде {FREE_MESSAGE_LIMIT} ТЕГІН сұрақ бар!**\n"
            f"*(Пакеттер: {STARS_PACK_PRICE} ⭐️ үшін {REQUESTS_PER_PACK} сұраныс)*\n\n"
            "Бастау үшін симптомыңызды немесе жағдайыңызды төменде сипаттаңыз:"
        ),
        "limit_reached": "Тегін және төленген сұраныстар аяқталды. Жалғастыру үшін жаңа пакет алыңыз:",
        "invoice_title": f"ИИ ассистентке {REQUESTS_PER_PACK} сұраныс",
        "invoice_desc": f"Психосоматика ИИ ассистентіне {REQUESTS_PER_PACK} қосымша сұраныс пакеті.",
        "invoice_label": f"{REQUESTS_PER_PACK} сұраныс",
        "payment_success": f"Төлем қабылданды! Сізге {REQUESTS_PER_PACK} сұраныс берілді. Жалғастыра беріңіз 🙌"
    },
    "es": {
        "welcome": (
            "¡Hola! 👋\n\n"
            "Te ayudo a descifrar lo que tu cuerpo (o el de tu hijo) intenta decirte "
            "a través de síntomas físicos, enfermedades y desencadenantes emocionales.\n\n"
            "💡 **¿No sabes cómo empezar? Envía un mensaje como:**\n"
            '• *"Mi hijo de 5 años tiene eccema constante en las manos."*\n'
            '• *"Tengo dolor lumbar desde hace 2 meses sin haberme lesionado."*\n'
            '• *"Siento apatía total y fatiga constante, aunque mis análisis médicos son normales."*\n\n'
            f"🎁 **¡Tienes {FREE_MESSAGE_LIMIT} preguntas GRATIS para empezar!**\n"
            f"*(Paquetes: {REQUESTS_PER_PACK} consultas por {STARS_PACK_PRICE} ⭐️)*\n\n"
            "Describe tu síntoma o estado a continuación para comenzar:"
        ),
        "limit_reached": "Se han agotado tus consultas gratuitas y pagadas. Consigue un nuevo paquete para continuar:",
        "invoice_title": f"{REQUESTS_PER_PACK} consultas al Asistente IA",
        "invoice_desc": f"Paquete de {REQUESTS_PER_PACK} consultas adicionales para el Asistente de Psicosomática IA.",
        "invoice_label": f"{REQUESTS_PER_PACK} consultas",
        "payment_success": f"¡Pago recibido! Se te han acreditado {REQUESTS_PER_PACK} consultas. Puedes continuar 🙌"
    },
    "fr": {
        "welcome": (
            "Bonjour ! 👋\n\n"
            "Je vous aide à décoder ce que votre corps (ou celui de votre enfant) essaie de vous dire "
            "à travers des symptômes physiques, des maladies et des déclencheurs émotionnels.\n\n"
            "💡 **Vous ne savez pas comment commencer ? Envoyez un message comme :**\n"
            '• *"Mon enfant de 5 ans a de l\'eczéma constant sur les mains."*\n'
            '• *"J\'ai mal au bas du dos depuis 2 mois, sans blessure."*\n'
            '• *"Je ressens une apathie totale et une fatigue constante, bien que mes analyses médicales soient normales."*\n\n'
            f"🎁 **Vous avez {FREE_MESSAGE_LIMIT} questions GRATUITES pour commencer !**\n"
            f"*(Forfaits : {REQUESTS_PER_PACK} requêtes pour {STARS_PACK_PRICE} ⭐️)*\n\n"
            "Décrivez votre symptôme ou votre état ci-dessous pour commencer :"
        ),
        "limit_reached": "Vous n'avez plus de requêtes gratuites ou payantes. Prenez un nouveau forfait pour continuer :",
        "invoice_title": f"{REQUESTS_PER_PACK} requêtes Assistant IA",
        "invoice_desc": f"Pack de {REQUESTS_PER_PACK} requêtes supplémentaires pour l'Assistant IA en Psychosomatique.",
        "invoice_label": f"{REQUESTS_PER_PACK} requêtes",
        "payment_success": f"Paiement reçu ! Vous avez crédité {REQUESTS_PER_PACK} requêtes. N'hésitez pas à continuer 🙌"
    },
    "de": {
        "welcome": (
            "Hallo! 👋\n\n"
            "Ich helfe dir zu entschlüsseln, was dein Körper (oder der deines Kindes) dir "
            "durch körperliche Symptome, Krankheiten und emotionale Auslöser sagen möchte.\n\n"
            "💡 **Weißt du nicht, wie du anfangen sollst? Sende einfach eine Nachricht wie:**\n"
            '• *"Mein 5-jähriges Kind hat ständiges Ekzem an den Händen."*\n'
            '• *"Ich habe seit 2 Monaten Rückenschmerzen, ohne Verletzung."*\n'
            '• *"Ich fühle totale Apathie und ständige Müdigkeit, obwohl meine medizinischen Tests normal sind."*\n\n'
            f"🎁 **Du hast {FREE_MESSAGE_LIMIT} KOSTENLOSE Fragen zum Start!**\n"
            f"*(Pakete: {REQUESTS_PER_PACK} Anfragen für {STARS_PACK_PRICE} ⭐️)*\n\n"
            "Beschreibe dein Symptom oder deinen Zustand unten, um zu beginnen:"
        ),
        "limit_reached": "Deine kostenlosen und bezahlten Anfragen sind aufgebraucht. Hole dir ein neues Paket, um fortzufahren:",
        "invoice_title": f"{REQUESTS_PER_PACK} KI-Assistent Anfragen",
        "invoice_desc": f"Paket mit {REQUESTS_PER_PACK} zusätzlichen Anfragen für den KI-Psychosomatik-Assistenten.",
        "invoice_label": f"{REQUESTS_PER_PACK} Anfragen",
        "payment_success": f"Zahlung erhalten! Dir wurden {REQUESTS_PER_PACK} Anfragen gutgeschrieben. Du kannst fortfahren 🙌"
    },
    "zh": {
        "welcome": (
            "你好！👋\n\n"
            "我致力于帮您解读身体（或您孩子的身体）通过身体症状、疾病和情绪诱因表达的声音。\n\n"
            "💡 **不知道如何开始？您可以这样发消息：**\n"
            '• *"我5岁的孩子手上一直长湿疹。"*\n'
            '• *"我腰痛了2个月，没有任何外伤。"*\n'
            '• *"虽然体检指标正常，但我感到彻底的冷漠和持续疲劳。"*\n\n'
            f"🎁 **开始体验，您拥有 {FREE_MESSAGE_LIMIT} 个免费提问额度！**\n"
            f"*(套餐：{REQUESTS_PER_PACK} 次咨询 / {STARS_PACK_PRICE} ⭐️)*\n\n"
            "请在下方描述您的症状或状态以开始："
        ),
        "limit_reached": "您的免费和付费咨询次数已用完。请获取新套餐以继续：",
        "invoice_title": f"{REQUESTS_PER_PACK} 次 AI 助手咨询",
        "invoice_desc": f"身心医学 AI 助手的 {REQUESTS_PER_PACK} 次额外咨询套餐。",
        "invoice_label": f"{REQUESTS_PER_PACK} 次咨询",
        "payment_success": f"已收到付款！您已获得 {REQUESTS_PER_PACK} 次咨询额度。欢迎继续 🙌"
    },
    "ar": {
        "welcome": (
            "مرحباً! 👋\n\n"
            "أساعدك في فك تشفير ما يحاول جسدك (أو جسد طفلك) إخبارَك به "
            "من خلال الأعراض الجسدية والأمراض والمحفزات العاطفية.\n\n"
            "💡 **لا تعرف كيف تبدأ؟ أرسل رسالة مثل:**\n"
            '• *"طفلي البالغ من العمر 5 سنوات يعاني من إكزيما مستمرة على يديه."*\n'
            '• *"أعاني من ألم في أسفل الظهر منذ شهرين دون إصابة."*\n'
            '• *"أشعر بفتور تام وإرهاق مستمر رغم أن الفحوصات الطبية سليمة."*\n\n'
            f"🎁 **لديك {FREE_MESSAGE_LIMIT} أسئلة مجانية للبدء!**\n"
            f"*(الباقات: {REQUESTS_PER_PACK} استفسار مقابل {STARS_PACK_PRICE} ⭐️)*\n\n"
            "صف أعراضك أو حالتك أدناه للبدء:"
        ),
        "limit_reached": "لقد استنفدت استفساراتك المجانية والمدفوعة. احصل على باقة جديدة للمتابعة:",
        "invoice_title": f"{REQUESTS_PER_PACK} استفسار لمساعد الذكاء الاصطناعي",
        "invoice_desc": f"باقة من {REQUESTS_PER_PACK} استفسار إضافي لمساعد النفسجسدية بالذكاء الاصطناعي.",
        "invoice_label": f"{REQUESTS_PER_PACK} استفسار",
        "payment_success": f"تم استلام الدفع! تم إضافة {REQUESTS_PER_PACK} استفسار لرصيدك. تفضل بالمتابعة 🙌"
    },
    "tr": {
        "welcome": (
            "Merhaba! 👋\n\n"
            "Bedeninizin (veya çocuğunuzun bedeninin) fiziksel semptomlar, hastalıklar ve "
            "duygusal tetikleyiciler aracılığıyla ne anlatmak istediğini çözmenize yardımcı oluyorum.\n\n"
            "💡 **Nasıl başlayacağınızı bilmiyor musunuz? Şunun gibi bir mesaj gönderin:**\n"
            '• *"5 yaşındaki çocuğumun ellerinde sürekli egzama var."*\n'
            '• *"Sakatlık olmamasına rağmen 2 aydır bel ağrısı çekiyorum."*\n'
            '• *"Tıbbi tahlillerim normal olmasına rağmen tam bir apati ve sürekli yorgunluk hissediyorum."*\n\n'
            f"🎁 **Başlamak için {FREE_MESSAGE_LIMIT} ÜCRETSİZ sorunuz var!**\n"
            f"*(Paketler: {STARS_PACK_PRICE} ⭐️ karşılığında {REQUESTS_PER_PACK} sorgу)*\n\n"
            "Başlamak için semptomunuzu veya durumunuzu aşağıda açıklayın:"
        ),
        "limit_reached": "Ücretsiz ve ödenmiş sorgularınız bitti. Devam etmek için yeni bir paket alın:",
        "invoice_title": f"{REQUESTS_PER_PACK} Yapay Zeka Asistanı Sorgusu",
        "invoice_desc": f"Psikosomatik Yapay Zeka Asistanı için {REQUESTS_PER_PACK} ek sorgu paketi.",
        "invoice_label": f"{REQUESTS_PER_PACK} sorgu",
        "payment_success": f"Ödeme alındı! Hesabınıza {REQUESTS_PER_PACK} sorgu tanımlandı. Devam edebilirsiniz 🙌"
    },
    "pt": {
        "welcome": (
            "Olá! 👋\n\n"
            "Ajudo a decodificar o que o seu corpo (ou o do seu filho) está tentando lhe dizer "
            "através de sintomas físicos, doenças e gatilhos emocionais.\n\n"
            "💡 **Não sabe como começar? Basta enviar uma mensagem como:**\n"
            '• *"Meu filho de 5 anos tem eczema constante nas mãos."*\n'
            '• *"Sinto dores na lombar há 2 meses, sem nenhuma lesão."*\n'
            '• *"Sinto apatia total e cansaço constante, embora meus exames estejam normais."*\n\n'
            f"🎁 **Você tem {FREE_MESSAGE_LIMIT} perguntas GRATUITAS para começar!**\n"
            f"*(Pacotes: {REQUESTS_PER_PACK} consultas por {STARS_PACK_PRICE} ⭐️)*\n\n"
            "Descreva seu sintoma ou estado abaixo para começar:"
        ),
        "limit_reached": "Suas consultas gratuitas e pagas acabaram. Adquira um novo pacote para continuar:",
        "invoice_title": f"{REQUESTS_PER_PACK} consultas ao Assistente IA",
        "invoice_desc": f"Pacote de {REQUESTS_PER_PACK} consultas adicionais para o Assistente de Psicossomática IA.",
        "invoice_label": f"{REQUESTS_PER_PACK} consultas",
        "payment_success": f"Pagamento recebido! Você recebeu {REQUESTS_PER_PACK} consultas. Fique à vontade para continuar 🙌"
    },
    "hi": {
        "welcome": (
            "नमस्ते! 👋\n\n"
            "मैं यह समझने में आपकी मदद करता हूं कि आपका शरीर (या आपके बच्चे का शरीर) "
            "शारीरिक लक्षणों, बीमारियों और भावनात्मक ट्रिगर्स के माध्यम से क्या कहने की कोशिश कर रहा है।\n\n"
            "💡 **समझ नहीं आ रहा कि कैसे शुरू करें? बस इस तरह का संदेश भेजें:**\n"
            '• *"मेरे 5 साल के बच्चे के हाथों पर लगातार एक्जिमा रहता है।"*\n'
            '• *"बिना किसी चोट के 2 महीने से मेरी कमर के निचले हिस्से में दर्द है।"*\n'
            '• *"मेडिकल रिपोर्ट सामान्य होने के बावजूद मुझे भारी थकान महसूस होती है।"*\n\n'
            f"🎁 **शुरुआत करने के लिए आपके पास {FREE_MESSAGE_LIMIT} मुफ्त प्रश्न हैं!**\n"
            f"*(पैकेज: {STARS_PACK_PRICE} ⭐️ में {REQUESTS_PER_PACK} प्रश्न)*\n\n"
            "शुरू करने के लिए नीचे अपने लक्षण या स्थिति का वर्णन करें:"
        ),
        "limit_reached": "आपके मुफ़्त और सशुल्क प्रश्न समाप्त हो गए हैं। जारी रखने के लिए नया पैक लें:",
        "invoice_title": f"{REQUESTS_PER_PACK} AI सहायक प्रश्न",
        "invoice_desc": f"मनोदैहिक AI सहायक के लिए {REQUESTS_PER_PACK} अतिरिक्त प्रश्नों का पैक।",
        "invoice_label": f"{REQUESTS_PER_PACK} प्रश्न",
        "payment_success": f"भुगतान प्राप्त हुआ! आपके खाते में {REQUESTS_PER_PACK} प्रश्न जोड़ दिए गए हैं। बेझिझक जारी रखें 🙌"
    },
    "ja": {
        "welcome": (
            "こんにちは！👋\n\n"
            "身体の症状、病気、感情のトリガーを通じて、あなたの身体（またはお子様の身体）が"
            "何を伝えようとしているのかを解読するお手伝いをします。\n\n"
            "💡 **使い方がわからない場合は、以下のように送信してみてください：**\n"
            '• *"5歳の子供の手に湿疹がずっと出ています。"*\n'
            '• *"怪我をしていないのに、2ヶ月前から腰痛があります。"*\n'
            '• *"検査結果は正常なのに、強い倦怠感と疲労感が続いています。"*\n\n'
            f"🎁 **初回は {FREE_MESSAGE_LIMIT} 回無料で質問できます！**\n"
            f"*(パック：{STARS_PACK_PRICE} ⭐️ で {REQUESTS_PER_PACK} 回質問可能)*\n\n"
            "始めるには、以下にあなたの症状や state を入力してください："
        ),
        "limit_reached": "無料および有料の質問回数が終了しました。続けるには新しいパックを取得してください：",
        "invoice_title": f"AIアシスタント質問 {REQUESTS_PER_PACK} 回分",
        "invoice_desc": f"心身症AIアシスタント用 {REQUESTS_PER_PACK} 回追加質問パック",
        "invoice_label": f"{REQUESTS_PER_PACK} 回質問",
        "payment_success": f"お支払いを受領しました！{REQUESTS_PER_PACK} 回分の質問が追加されました。そのままお続けください 🙌"
    },
    "it": {
        "welcome": (
            "Ciao! 👋\n\n"
            "Ti aiuto a decodificare ciò che il tuo corpo (o quello del tuo bambino) sta cercando di dirti "
            "attraverso sintomi fisici, malattie e trigger emotivi.\n\n"
            "💡 **Non sai come iniziare? Invia semplicemente un messaggio come:**\n"
            '• *"Il mio bambino di 5 anni ha un eczema costante sulle mani."*\n'
            '• *"Ho mal di schiena da 2 mesi, senza aver subito lesioni."*\n'
            '• *"Sento una totale apatia e stanchezza costante, anche se le mie analisi mediche sono normali."*\n\n'
            f"🎁 **Hai {FREE_MESSAGE_LIMIT} domande GRATUITE per iniziare!**\n"
            f"*(Pacchetti: {REQUESTS_PER_PACK} richieste per {STARS_PACK_PRICE} ⭐️️)*\n\n"
            "Descrivi il tuo sintomo o il tuo stato qui sotto per iniziare:"
        ),
        "limit_reached": "Hai esaurito le richieste gratuite e a pagamento. Acquista un nuovo pacchetto per continuare:",
        "invoice_title": f"{REQUESTS_PER_PACK} richieste Assistente IA",
        "invoice_desc": f"Pacchetto di {REQUESTS_PER_PACK} richieste aggiuntive per l'Assistente IA di Psicosomatica.",
        "invoice_label": f"{REQUESTS_PER_PACK} richieste",
        "payment_success": f"Pagamento ricevuto! Ti sono state accreditate {REQUESTS_PER_PACK} richieste. Continua pure 🙌"
    },
    "ko": {
        "welcome": (
            "안녕하세요! 👋\n\n"
            "신체적 증상, 질병, 감정적 트ริ거를 통해 당신의 몸(또는 자녀의 몸)이 "
            "무엇을 말하려 하는지 해독하는 것을 도와드립니다.\n\n"
            "💡 **어떻게 시작해야 할지 모르겠다면 다음과 같이 메시지를 보내보세요:**\n"
            '• *"5살 아이 손에 습진이 계속 생겨요."*\n'
            '• *"다친 적이 없는데 2달 전부터 허리 통증이 있어요."*\n'
            '• *"병원 검사 결과는 정상인데 무기력하고 계속 피곤해요."*\n\n'
            f"🎁 **시작을 위해 {FREE_MESSAGE_LIMIT}개의 무료 질문이 제공됩니다!**\n"
            f"*(패키지: {STARS_PACK_PRICE} ⭐️에 {REQUESTS_PER_PACK}개 질문)*\n\n"
            "시작하려면 아래에 증상이나 상태를 설명해주세요:"
        ),
        "limit_reached": "무료 및 유료 질문이 모두 소진되었습니다. 계속하려면 새 패키지를 구매하세요:",
        "invoice_title": f"AI 어시스턴트 질문 {REQUESTS_PER_PACK}개",
        "invoice_desc": f"심신의학 AI 어시스턴트를 위한 {REQUESTS_PER_PACK}개 추가 질문 패키지",
        "invoice_label": f"질문 {REQUESTS_PER_PACK}개",
        "payment_success": f"결제가 완료되었습니다! {REQUESTS_PER_PACK}개의 질문이 충전되었습니다. 자유롭게 계속하세요 🙌"
    }
}
