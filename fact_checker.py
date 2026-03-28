def analyze_claim(claim):

    claim = claim.lower()

    # -------------------------------
    # SOCIAL MEDIA MISINFORMATION DB
    # -------------------------------

    misinformation_db = {

        # ₹2000 NOTE RUMOR
        "₹2000 notes will be completely banned immediately and become invalid overnight": {
            "result": "Refuted",
            "confidence": 95,
            "explanation": "RBI clarified that ₹2000 notes remain legal tender and can still be deposited or exchanged.",
            "manipulation": "WhatsApp financial rumor",
            "contradictions": "Contradicts RBI official statement",
            "source": "Reserve Bank of India"
        },

        "₹2000 के नोट तत्काल प्रभाव से पूरी तरह प्रतिबंधित कर दिए जाएंगे और रातोंरात अमान्य हो जाएंगे": {
            "result": "Refuted",
            "confidence": 95,
            "explanation": "RBI ने स्पष्ट किया कि ₹2000 के नोट अभी भी वैध मुद्रा हैं और बैंक में जमा या बदले जा सकते हैं।",
            "manipulation": "व्हाट्सएप पर फैल रही वित्तीय अफवाह",
            "contradictions": "RBI की आधिकारिक घोषणा के विपरीत",
            "source": "Reserve Bank of India"
        },

        # PETROL RUMOR
        "petrol and diesel will run out soon in india": {
            "result": "Refuted",
            "confidence": 94,
            "explanation": "Government and oil companies confirmed there was no fuel shortage. The rumor caused panic buying.",
            "manipulation": "Panic rumor circulating on social media",
            "contradictions": "Contradicts official fuel supply reports",
            "source": "Indian Oil Corporation"
        },

        "भारत में जल्द ही पेट्रोल और डीजल खत्म हो जाएंगे": {
            "result": "Refuted",
            "confidence": 94,
            "explanation": "सरकार और तेल कंपनियों ने स्पष्ट किया कि देश में ईंधन की कोई कमी नहीं है।",
            "manipulation": "सोशल मीडिया पर फैली अफवाह",
            "contradictions": "आधिकारिक ईंधन आपूर्ति रिपोर्ट के विपरीत",
            "source": "Indian Oil Corporation"
        },

        # JEE PAPER LEAK
        "jee main 2026 question paper has leaked": {
            "result": "Refuted",
            "confidence": 96,
            "explanation": "The National Testing Agency confirmed that no paper leak occurred and warned students about scams.",
            "manipulation": "Exam scam misinformation",
            "contradictions": "Contradicts NTA official announcement",
            "source": "National Testing Agency"
        },

        "jee main 2026 का प्रश्न पत्र लीक हो गया है": {
            "result": "Refuted",
            "confidence": 96,
            "explanation": "राष्ट्रीय परीक्षण एजेंसी (NTA) ने पुष्टि की कि कोई पेपर लीक नहीं हुआ है।",
            "manipulation": "परीक्षा से जुड़ी फर्जी खबर",
            "contradictions": "NTA की आधिकारिक घोषणा के विपरीत",
            "source": "National Testing Agency"
        },

        # INDIA PAKISTAN NUCLEAR CLAIM
        "india attacked pakistan kirana hills nuclear site": {
            "result": "Refuted",
            "confidence": 97,
            "explanation": "The claim was based on a fake document and no such nuclear incident occurred.",
            "manipulation": "Geopolitical misinformation spread online",
            "contradictions": "Contradicts international news reports",
            "source": "Global News Agencies"
        },

        "भारत ने पाकिस्तान के किराना हिल्स परमाणु स्थल पर हमला किया": {
            "result": "Refuted",
            "confidence": 97,
            "explanation": "यह दावा एक फर्जी दस्तावेज़ पर आधारित था और ऐसा कोई परमाणु हमला नहीं हुआ।",
            "manipulation": "भ्रामक भू-राजनीतिक अफवाह",
            "contradictions": "अंतरराष्ट्रीय समाचार रिपोर्टों के विपरीत",
            "source": "Global News Agencies"
        },

        # COVID VARIANT CLAIM
        "new deadly covid variant spreading rapidly across india": {
            "result": "Refuted",
            "confidence": 93,
            "explanation": "Health authorities confirmed that no emergency COVID variant outbreak was occurring.",
            "manipulation": "Health panic misinformation",
            "contradictions": "Contradicts official health ministry reports",
            "source": "WHO / Indian Health Ministry"
        },

        "भारत में नया खतरनाक कोविड वैरिएंट तेजी से फैल रहा है": {
            "result": "Refuted",
            "confidence": 93,
            "explanation": "स्वास्थ्य अधिकारियों ने पुष्टि की कि ऐसा कोई नया आपातकालीन कोविड वैरिएंट नहीं फैल रहा है।",
            "manipulation": "स्वास्थ्य से जुड़ी अफवाह",
            "contradictions": "स्वास्थ्य मंत्रालय की रिपोर्ट के विपरीत",
            "source": "WHO / Indian Health Ministry"
        }

    }

    # --------------------------------
    # CHECK MISINFORMATION CLAIMS
    # --------------------------------

    for key in misinformation_db:
        if key.lower() in claim:
            return misinformation_db[key]

    # --------------------------------
    # GENERAL FACT CHECK LOGIC
    # --------------------------------

    if "covid" in claim or "pandemic" in claim or "कोविड" in claim:
        return {
            "result": "Supported",
            "confidence": 90,
            "explanation": "COVID-19 was declared a global pandemic by the World Health Organization.",
            "manipulation": "No misinformation pattern",
            "contradictions": "None",
            "source": "WHO"
        }

    if "earth is flat" in claim or "पृथ्वी सपाट है" in claim:
        return {
            "result": "Refuted",
            "confidence": 98,
            "explanation": "Scientific consensus proves Earth is spherical.",
            "manipulation": "Common internet conspiracy",
            "contradictions": "Contradicts astronomy and satellite data",
            "source": "NASA"
        }

    if ("iran" in claim and "us" in claim) or ("ईरान" in claim and "अमेरिका" in claim):
        return {
            "result": "Supported",
            "confidence": 85,
            "explanation": "Iran and the United States have had decades of geopolitical tensions.",
            "manipulation": "No misinformation detected",
            "contradictions": "None",
            "source": "Global News Reports"
        }

    # --------------------------------
    # DEFAULT RESPONSE
    # --------------------------------

    return {
        "result": "Uncertain",
        "confidence": 70,
        "explanation": "The system could not find strong verified evidence for this claim.",
        "manipulation": "Unknown",
        "contradictions": "Limited evidence",
        "source": "AI Claim Analyzer"
    }