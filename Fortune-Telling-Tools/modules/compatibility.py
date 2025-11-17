# 匹配度分析模块
"""
基于星座和MBTI的匹配度分析
包括：情感匹配度、生活匹配度、事业匹配度
"""

# 星座匹配度数据
ZODIAC_COMPATIBILITY = {
    "白羊座": {
        "情感匹配": {
            "极佳": ["狮子座", "射手座", "双子座"],
            "良好": ["天秤座", "水瓶座", "白羊座"],
            "一般": ["金牛座", "处女座", "摩羯座"],
            "较差": ["巨蟹座", "天蝎座", "双鱼座"]
        },
        "生活匹配": {
            "极佳": ["狮子座", "射手座"],
            "良好": ["双子座", "天秤座"],
            "一般": ["水瓶座", "白羊座"],
            "较差": ["金牛座", "处女座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        },
        "事业匹配": {
            "极佳": ["狮子座", "射手座", "天秤座"],
            "良好": ["双子座", "水瓶座", "白羊座"],
            "一般": ["金牛座", "处女座", "摩羯座"],
            "较差": ["巨蟹座", "天蝎座", "双鱼座"]
        }
    },
    "金牛座": {
        "情感匹配": {
            "极佳": ["处女座", "摩羯座", "巨蟹座"],
            "良好": ["天蝎座", "双鱼座", "金牛座"],
            "一般": ["双子座", "天秤座", "水瓶座"],
            "较差": ["白羊座", "狮子座", "射手座"]
        },
        "生活匹配": {
            "极佳": ["处女座", "摩羯座"],
            "良好": ["巨蟹座", "天蝎座"],
            "一般": ["双鱼座", "金牛座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "天秤座", "水瓶座"]
        },
        "事业匹配": {
            "极佳": ["处女座", "摩羯座", "天蝎座"],
            "良好": ["巨蟹座", "金牛座"],
            "一般": ["双鱼座", "天秤座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "水瓶座"]
        }
    },
    "双子座": {
        "情感匹配": {
            "极佳": ["天秤座", "水瓶座", "狮子座"],
            "良好": ["白羊座", "射手座", "双子座"],
            "一般": ["巨蟹座", "天蝎座", "双鱼座"],
            "较差": ["金牛座", "处女座", "摩羯座"]
        },
        "生活匹配": {
            "极佳": ["天秤座", "水瓶座"],
            "良好": ["狮子座", "射手座", "双子座"],
            "一般": ["白羊座"],
            "较差": ["金牛座", "处女座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        },
        "事业匹配": {
            "极佳": ["天秤座", "水瓶座", "狮子座"],
            "良好": ["双子座", "射手座"],
            "一般": ["白羊座", "处女座"],
            "较差": ["金牛座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        }
    },
    "巨蟹座": {
        "情感匹配": {
            "极佳": ["天蝎座", "双鱼座", "金牛座"],
            "良好": ["处女座", "摩羯座", "巨蟹座"],
            "一般": ["双子座", "天秤座", "水瓶座"],
            "较差": ["白羊座", "狮子座", "射手座"]
        },
        "生活匹配": {
            "极佳": ["天蝎座", "双鱼座"],
            "良好": ["金牛座", "处女座"],
            "一般": ["摩羯座", "巨蟹座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "天秤座", "水瓶座"]
        },
        "事业匹配": {
            "极佳": ["天蝎座", "金牛座", "处女座"],
            "良好": ["双鱼座", "摩羯座"],
            "一般": ["巨蟹座", "天秤座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "水瓶座"]
        }
    },
    "狮子座": {
        "情感匹配": {
            "极佳": ["射手座", "白羊座", "天秤座"],
            "良好": ["双子座", "狮子座", "水瓶座"],
            "一般": ["金牛座", "处女座", "摩羯座"],
            "较差": ["巨蟹座", "天蝎座", "双鱼座"]
        },
        "生活匹配": {
            "极佳": ["射手座", "白羊座"],
            "良好": ["天秤座", "狮子座"],
            "一般": ["双子座", "水瓶座"],
            "较差": ["金牛座", "处女座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        },
        "事业匹配": {
            "极佳": ["射手座", "白羊座", "天秤座"],
            "良好": ["狮子座", "双子座"],
            "一般": ["水瓶座", "处女座"],
            "较差": ["金牛座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        }
    },
    "处女座": {
        "情感匹配": {
            "极佳": ["摩羯座", "金牛座", "天蝎座"],
            "良好": ["巨蟹座", "双鱼座", "处女座"],
            "一般": ["双子座", "天秤座", "水瓶座"],
            "较差": ["白羊座", "狮子座", "射手座"]
        },
        "生活匹配": {
            "极佳": ["摩羯座", "金牛座"],
            "良好": ["天蝎座", "处女座"],
            "一般": ["巨蟹座", "双鱼座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "天秤座", "水瓶座"]
        },
        "事业匹配": {
            "极佳": ["摩羯座", "金牛座", "天蝎座"],
            "良好": ["处女座", "巨蟹座"],
            "一般": ["双鱼座", "天秤座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "水瓶座"]
        }
    },
    "天秤座": {
        "情感匹配": {
            "极佳": ["水瓶座", "双子座", "狮子座"],
            "良好": ["射手座", "天秤座", "白羊座"],
            "一般": ["巨蟹座", "天蝎座", "双鱼座"],
            "较差": ["金牛座", "处女座", "摩羯座"]
        },
        "生活匹配": {
            "极佳": ["水瓶座", "双子座"],
            "良好": ["狮子座", "天秤座"],
            "一般": ["射手座", "白羊座"],
            "较差": ["金牛座", "处女座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        },
        "事业匹配": {
            "极佳": ["水瓶座", "双子座", "狮子座"],
            "良好": ["天秤座", "射手座"],
            "一般": ["白羊座", "处女座"],
            "较差": ["金牛座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        }
    },
    "天蝎座": {
        "情感匹配": {
            "极佳": ["双鱼座", "巨蟹座", "摩羯座"],
            "良好": ["金牛座", "处女座", "天蝎座"],
            "一般": ["双子座", "天秤座", "水瓶座"],
            "较差": ["白羊座", "狮子座", "射手座"]
        },
        "生活匹配": {
            "极佳": ["双鱼座", "巨蟹座"],
            "良好": ["摩羯座", "天蝎座"],
            "一般": ["金牛座", "处女座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "天秤座", "水瓶座"]
        },
        "事业匹配": {
            "极佳": ["双鱼座", "摩羯座", "金牛座"],
            "良好": ["巨蟹座", "天蝎座"],
            "一般": ["处女座", "天秤座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "水瓶座"]
        }
    },
    "射手座": {
        "情感匹配": {
            "极佳": ["白羊座", "狮子座", "天秤座"],
            "良好": ["双子座", "水瓶座", "射手座"],
            "一般": ["金牛座", "处女座", "摩羯座"],
            "较差": ["巨蟹座", "天蝎座", "双鱼座"]
        },
        "生活匹配": {
            "极佳": ["白羊座", "狮子座"],
            "良好": ["天秤座", "射手座"],
            "一般": ["双子座", "水瓶座"],
            "较差": ["金牛座", "处女座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        },
        "事业匹配": {
            "极佳": ["白羊座", "狮子座", "天秤座"],
            "良好": ["射手座", "双子座"],
            "一般": ["水瓶座", "处女座"],
            "较差": ["金牛座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        }
    },
    "摩羯座": {
        "情感匹配": {
            "极佳": ["金牛座", "处女座", "天蝎座"],
            "良好": ["巨蟹座", "双鱼座", "摩羯座"],
            "一般": ["双子座", "天秤座", "水瓶座"],
            "较差": ["白羊座", "狮子座", "射手座"]
        },
        "生活匹配": {
            "极佳": ["金牛座", "处女座"],
            "良好": ["天蝎座", "摩羯座"],
            "一般": ["巨蟹座", "双鱼座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "天秤座", "水瓶座"]
        },
        "事业匹配": {
            "极佳": ["金牛座", "处女座", "天蝎座"],
            "良好": ["摩羯座", "巨蟹座"],
            "一般": ["双鱼座", "天秤座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "水瓶座"]
        }
    },
    "水瓶座": {
        "情感匹配": {
            "极佳": ["双子座", "天秤座", "白羊座"],
            "良好": ["狮子座", "射手座", "水瓶座"],
            "一般": ["巨蟹座", "天蝎座", "双鱼座"],
            "较差": ["金牛座", "处女座", "摩羯座"]
        },
        "生活匹配": {
            "极佳": ["双子座", "天秤座"],
            "良好": ["白羊座", "水瓶座"],
            "一般": ["狮子座", "射手座"],
            "较差": ["金牛座", "处女座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        },
        "事业匹配": {
            "极佳": ["双子座", "天秤座", "白羊座"],
            "良好": ["水瓶座", "狮子座"],
            "一般": ["射手座", "处女座"],
            "较差": ["金牛座", "摩羯座", "巨蟹座", "天蝎座", "双鱼座"]
        }
    },
    "双鱼座": {
        "情感匹配": {
            "极佳": ["巨蟹座", "天蝎座", "金牛座"],
            "良好": ["处女座", "摩羯座", "双鱼座"],
            "一般": ["双子座", "天秤座", "水瓶座"],
            "较差": ["白羊座", "狮子座", "射手座"]
        },
        "生活匹配": {
            "极佳": ["巨蟹座", "天蝎座"],
            "良好": ["金牛座", "双鱼座"],
            "一般": ["处女座", "摩羯座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "天秤座", "水瓶座"]
        },
        "事业匹配": {
            "极佳": ["巨蟹座", "天蝎座", "金牛座"],
            "良好": ["双鱼座", "处女座"],
            "一般": ["摩羯座", "天秤座"],
            "较差": ["白羊座", "狮子座", "射手座", "双子座", "水瓶座"]
        }
    }
}

# MBTI匹配度数据
MBTI_COMPATIBILITY = {
    "INTJ": {
        "情感匹配": {
            "极佳": ["ENFP", "ENTP"],
            "良好": ["INFJ", "INFP", "INTJ"],
            "一般": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
            "较差": ["ESFP", "ISFP", "ESTP", "ISTP"]
        },
        "生活匹配": {
            "极佳": ["ENFP", "ENTP"],
            "良好": ["INFJ", "INFP"],
            "一般": ["INTJ", "ISTJ", "ISFJ"],
            "较差": ["ESFP", "ISFP", "ESTP", "ISTP", "ESTJ", "ESFJ"]
        },
        "事业匹配": {
            "极佳": ["ENTJ", "ENTP"],
            "良好": ["INTJ", "INFJ", "INTP"],
            "一般": ["ISTJ", "ISFJ", "ESTJ"],
            "较差": ["ESFP", "ISFP", "ESTP", "ISTP", "ESFJ"]
        }
    },
    "INTP": {
        "情感匹配": {
            "极佳": ["ENTJ", "ESTJ"],
            "良好": ["INTJ", "INFP", "INTP"],
            "一般": ["ISTP", "ISFP", "ESTP", "ESFP"],
            "较差": ["ENFJ", "ESFJ", "ISFJ"]
        },
        "生活匹配": {
            "极佳": ["ENTJ", "ESTJ"],
            "良好": ["INTJ", "INFP"],
            "一般": ["INTP", "ISTP", "ISFP"],
            "较差": ["ENFJ", "ESFJ", "ISFJ", "ESFP", "ESTP"]
        },
        "事业匹配": {
            "极佳": ["ENTJ", "ESTJ"],
            "良好": ["INTJ", "INTP", "ENTP"],
            "一般": ["ISTP", "ISFP", "ESTP"],
            "较差": ["ENFJ", "ESFJ", "ISFJ", "ESFP"]
        }
    },
    "ENTJ": {
        "情感匹配": {
            "极佳": ["INFP", "ISFP"],
            "良好": ["INTJ", "INTP", "ENTJ"],
            "一般": ["ESTJ", "ESFJ", "ISTJ", "ISFJ"],
            "较差": ["ENFJ", "ESFP"]
        },
        "生活匹配": {
            "极佳": ["INFP", "ISFP"],
            "良好": ["INTJ", "INTP"],
            "一般": ["ENTJ", "ESTJ", "ESFJ"],
            "较差": ["ENFJ", "ESFP", "ISTP", "ESTP"]
        },
        "事业匹配": {
            "极佳": ["INTP", "INTJ"],
            "良好": ["ENTJ", "ENTP", "ESTJ"],
            "一般": ["ISTJ", "ISFJ", "ESFJ"],
            "较差": ["ENFJ", "ESFP", "ISFP", "INFP"]
        }
    },
    "ENTP": {
        "情感匹配": {
            "极佳": ["INFJ", "INTJ"],
            "良好": ["ENFP", "INFP", "ENTP"],
            "一般": ["ESTP", "ESFP", "ISTP", "ISFP"],
            "较差": ["ENFJ", "ESFJ"]
        },
        "生活匹配": {
            "极佳": ["INFJ", "INTJ"],
            "良好": ["ENFP", "INFP"],
            "一般": ["ENTP", "ESTP", "ESFP"],
            "较差": ["ENFJ", "ESFJ", "ISFJ", "ISTJ"]
        },
        "事业匹配": {
            "极佳": ["INTJ", "INFJ"],
            "良好": ["ENTP", "ENTJ", "ENFP"],
            "一般": ["ESTP", "ESFP", "ISTP"],
            "较差": ["ENFJ", "ESFJ", "ISFJ", "ISTJ"]
        }
    },
    "INFJ": {
        "情感匹配": {
            "极佳": ["ENFP", "ENTP"],
            "良好": ["INFP", "INTJ", "INFJ"],
            "一般": ["ISFJ", "ISTJ", "ESFJ", "ESTJ"],
            "较差": ["ESFP", "ISFP"]
        },
        "生活匹配": {
            "极佳": ["ENFP", "ENTP"],
            "良好": ["INFP", "INTJ"],
            "一般": ["INFJ", "ISFJ", "ISTJ"],
            "较差": ["ESFP", "ISFP", "ESTP", "ISTP"]
        },
        "事业匹配": {
            "极佳": ["ENFP", "ENTP"],
            "良好": ["INFJ", "INTJ", "INFP"],
            "一般": ["ISFJ", "ISTJ", "ESFJ"],
            "较差": ["ESFP", "ISFP", "ESTP", "ISTP"]
        }
    },
    "INFP": {
        "情感匹配": {
            "极佳": ["ENTJ", "ESTJ"],
            "良好": ["INFJ", "INTP", "INFP"],
            "一般": ["ISFP", "ISTP", "ESFP", "ESTP"],
            "较差": ["ENFJ", "ESFJ"]
        },
        "生活匹配": {
            "极佳": ["ENTJ", "ESTJ"],
            "良好": ["INFJ", "INTP"],
            "一般": ["INFP", "ISFP", "ISTP"],
            "较差": ["ENFJ", "ESFJ", "ISFJ", "ISTJ"]
        },
        "事业匹配": {
            "极佳": ["ENTJ", "ESTJ"],
            "良好": ["INFJ", "INTP", "INFP"],
            "一般": ["ISFP", "ISTP", "ESFP"],
            "较差": ["ENFJ", "ESFJ", "ISFJ", "ISTJ"]
        }
    },
    "ENFJ": {
        "情感匹配": {
            "极佳": ["INFP", "ISFP"],
            "良好": ["INFJ", "INTJ", "ENFJ"],
            "一般": ["ESFJ", "ESTJ", "ISTJ", "ISFJ"],
            "较差": ["ENTP", "ESTP"]
        },
        "生活匹配": {
            "极佳": ["INFP", "ISFP"],
            "良好": ["INFJ", "INTJ"],
            "一般": ["ENFJ", "ESFJ", "ESTJ"],
            "较差": ["ENTP", "ESTP", "ISTP", "ESFP"]
        },
        "事业匹配": {
            "极佳": ["INFP", "ISFP"],
            "良好": ["INFJ", "INTJ", "ENFJ"],
            "一般": ["ESFJ", "ESTJ", "ISTJ"],
            "较差": ["ENTP", "ESTP", "ISTP", "ESFP"]
        }
    },
    "ENFP": {
        "情感匹配": {
            "极佳": ["INTJ", "INFJ"],
            "良好": ["INFP", "ENTP", "ENFP"],
            "一般": ["ESFP", "ESTP", "ISFP", "ISTP"],
            "较差": ["ENTJ", "ESTJ"]
        },
        "生活匹配": {
            "极佳": ["INTJ", "INFJ"],
            "良好": ["INFP", "ENTP"],
            "一般": ["ENFP", "ESFP", "ESTP"],
            "较差": ["ENTJ", "ESTJ", "ISFJ", "ISTJ"]
        },
        "事业匹配": {
            "极佳": ["INTJ", "INFJ"],
            "良好": ["ENFP", "ENTP", "INFP"],
            "一般": ["ESFP", "ESTP", "ISFP"],
            "较差": ["ENTJ", "ESTJ", "ISFJ", "ISTJ"]
        }
    },
    "ISTJ": {
        "情感匹配": {
            "极佳": ["ESFP", "ESTP"],
            "良好": ["ISFJ", "ISTP", "ISTJ"],
            "一般": ["ENTJ", "ENFJ", "INTJ", "INFJ"],
            "较差": ["ENFP", "INFP"]
        },
        "生活匹配": {
            "极佳": ["ESFP", "ESTP"],
            "良好": ["ISFJ", "ISTP"],
            "一般": ["ISTJ", "ESTJ", "ESFJ"],
            "较差": ["ENFP", "INFP", "ENTP", "ENFJ"]
        },
        "事业匹配": {
            "极佳": ["ESFP", "ESTP"],
            "良好": ["ISTJ", "ISFJ", "ESTJ"],
            "一般": ["ISTP", "ISFP", "ESFJ"],
            "较差": ["ENFP", "INFP", "ENTP", "ENFJ"]
        }
    },
    "ISFJ": {
        "情感匹配": {
            "极佳": ["ESTP", "ESFP"],
            "良好": ["ISTJ", "ISFP", "ISFJ"],
            "一般": ["ENFJ", "ENTJ", "INFJ", "INTJ"],
            "较差": ["ENFP", "INFP"]
        },
        "生活匹配": {
            "极佳": ["ESTP", "ESFP"],
            "良好": ["ISTJ", "ISFP"],
            "一般": ["ISFJ", "ESTJ", "ESFJ"],
            "较差": ["ENFP", "INFP", "ENTP", "ENFJ"]
        },
        "事业匹配": {
            "极佳": ["ESTP", "ESFP"],
            "良好": ["ISFJ", "ISTJ", "ESTJ"],
            "一般": ["ISFP", "ISTP", "ESFJ"],
            "较差": ["ENFP", "INFP", "ENTP", "ENFJ"]
        }
    },
    "ESTJ": {
        "情感匹配": {
            "极佳": ["INFP", "ISFP"],
            "良好": ["ISTJ", "ISFJ", "ESTJ"],
            "一般": ["ENTJ", "ENFJ", "INTJ", "INFJ"],
            "较差": ["ENFP", "INTP"]
        },
        "生活匹配": {
            "极佳": ["INFP", "ISFP"],
            "良好": ["ISTJ", "ISFJ"],
            "一般": ["ESTJ", "ESFJ", "ESTP"],
            "较差": ["ENFP", "INTP", "ENTP", "ENFJ"]
        },
        "事业匹配": {
            "极佳": ["INFP", "ISFP"],
            "良好": ["ISTJ", "ISFJ", "ESTJ"],
            "一般": ["ESFJ", "ESTP", "ESFP"],
            "较差": ["ENFP", "INTP", "ENTP", "ENFJ"]
        }
    },
    "ESFJ": {
        "情感匹配": {
            "极佳": ["ISTP", "INTP"],
            "良好": ["ISFJ", "ESTJ", "ESFJ"],
            "一般": ["ENFJ", "ENTJ", "INFJ", "INTJ"],
            "较差": ["ENFP", "INFP"]
        },
        "生活匹配": {
            "极佳": ["ISTP", "INTP"],
            "良好": ["ISFJ", "ESTJ"],
            "一般": ["ESFJ", "ESFP", "ESTP"],
            "较差": ["ENFP", "INFP", "ENTP", "ENFJ"]
        },
        "事业匹配": {
            "极佳": ["ISTP", "INTP"],
            "良好": ["ISFJ", "ESTJ", "ESFJ"],
            "一般": ["ESFP", "ESTP", "ISFP"],
            "较差": ["ENFP", "INFP", "ENTP", "ENFJ"]
        }
    },
    "ISTP": {
        "情感匹配": {
            "极佳": ["ESFJ", "ENFJ"],
            "良好": ["ISTJ", "ISFJ", "ISTP"],
            "一般": ["ENTP", "ENFP", "INTP", "INFP"],
            "较差": ["ESTJ", "ENTJ"]
        },
        "生活匹配": {
            "极佳": ["ESFJ", "ENFJ"],
            "良好": ["ISTJ", "ISFJ"],
            "一般": ["ISTP", "ISFP", "ESTP"],
            "较差": ["ESTJ", "ENTJ", "ENTP", "ENFP"]
        },
        "事业匹配": {
            "极佳": ["ESFJ", "ENFJ"],
            "良好": ["ISTP", "ISTJ", "ISFJ"],
            "一般": ["ISFP", "ESTP", "ESFP"],
            "较差": ["ESTJ", "ENTJ", "ENTP", "ENFP"]
        }
    },
    "ISFP": {
        "情感匹配": {
            "极佳": ["ESTJ", "ENTJ"],
            "良好": ["ISFJ", "ISTJ", "ISFP"],
            "一般": ["ENFP", "ENTP", "INFP", "INTP"],
            "较差": ["ESFJ", "ENFJ"]
        },
        "生活匹配": {
            "极佳": ["ESTJ", "ENTJ"],
            "良好": ["ISFJ", "ISTJ"],
            "一般": ["ISFP", "ISTP", "ESFP"],
            "较差": ["ESFJ", "ENFJ", "ENTP", "ENFP"]
        },
        "事业匹配": {
            "极佳": ["ESTJ", "ENTJ"],
            "良好": ["ISFP", "ISFJ", "ISTJ"],
            "一般": ["ISTP", "ESFP", "ESTP"],
            "较差": ["ESFJ", "ENFJ", "ENTP", "ENFP"]
        }
    },
    "ESTP": {
        "情感匹配": {
            "极佳": ["ISFJ", "ISTJ"],
            "良好": ["ESFP", "ENFP", "ESTP"],
            "一般": ["INTP", "INFP", "ENTP", "ENFJ"],
            "较差": ["INTJ", "INFJ"]
        },
        "生活匹配": {
            "极佳": ["ISFJ", "ISTJ"],
            "良好": ["ESFP", "ENFP"],
            "一般": ["ESTP", "ISTP", "ESFJ"],
            "较差": ["INTJ", "INFJ", "ENTP", "ENFJ"]
        },
        "事业匹配": {
            "极佳": ["ISFJ", "ISTJ"],
            "良好": ["ESTP", "ESFP", "ENFP"],
            "一般": ["ISTP", "ISFP", "ESFJ"],
            "较差": ["INTJ", "INFJ", "ENTP", "ENFJ"]
        }
    },
    "ESFP": {
        "情感匹配": {
            "极佳": ["ISTJ", "ISFJ"],
            "良好": ["ESTP", "ENTP", "ESFP"],
            "一般": ["INFP", "INFJ", "INTJ", "INTP"],
            "较差": ["ENTJ", "ENFJ"]
        },
        "生活匹配": {
            "极佳": ["ISTJ", "ISFJ"],
            "良好": ["ESTP", "ENTP"],
            "一般": ["ESFP", "ISFP", "ESTJ"],
            "较差": ["ENTJ", "ENFJ", "ENTP", "ENFP"]
        },
        "事业匹配": {
            "极佳": ["ISTJ", "ISFJ"],
            "良好": ["ESFP", "ESTP", "ENTP"],
            "一般": ["ISFP", "ISTP", "ESTJ"],
            "较差": ["ENTJ", "ENFJ", "ENTP", "ENFP"]
        }
    }
}


def get_compatibility_score(level):
    """获取匹配度分数"""
    score_map = {
        "极佳": 95,
        "良好": 75,
        "一般": 55,
        "较差": 35
    }
    return score_map.get(level, 50)


def analyze_zodiac_compatibility(zodiac1, zodiac2):
    """
    分析两个星座的匹配度
    
    参数:
        zodiac1: 第一个星座
        zodiac2: 第二个星座
    
    返回:
        匹配度分析字典
    """
    if zodiac1 not in ZODIAC_COMPATIBILITY:
        return None
    
    compatibility_data = ZODIAC_COMPATIBILITY[zodiac1]
    
    result = {
        "zodiac1": zodiac1,
        "zodiac2": zodiac2,
        "情感匹配": {"level": "一般", "score": 50, "description": ""},
        "生活匹配": {"level": "一般", "score": 50, "description": ""},
        "事业匹配": {"level": "一般", "score": 50, "description": ""},
        "综合匹配": {"score": 50, "level": "一般", "description": ""}
    }
    
    # 分析各个维度的匹配度
    for dimension in ["情感匹配", "生活匹配", "事业匹配"]:
        dimension_data = compatibility_data.get(dimension, {})
        level = "一般"
        
        for match_level, zodiacs in dimension_data.items():
            if zodiac2 in zodiacs:
                level = match_level
                break
        
        score = get_compatibility_score(level)
        result[dimension] = {
            "level": level,
            "score": score,
            "description": f"{zodiac1}与{zodiac2}在{dimension}方面匹配度为{level}（{score}分）"
        }
    
    # 计算综合匹配度
    total_score = (
        result["情感匹配"]["score"] +
        result["生活匹配"]["score"] +
        result["事业匹配"]["score"]
    ) / 3
    
    if total_score >= 85:
        overall_level = "极佳"
    elif total_score >= 70:
        overall_level = "良好"
    elif total_score >= 50:
        overall_level = "一般"
    else:
        overall_level = "较差"
    
    result["综合匹配"] = {
        "score": int(total_score),
        "level": overall_level,
        "description": f"{zodiac1}与{zodiac2}的综合匹配度为{overall_level}（{int(total_score)}分）"
    }
    
    return result


def analyze_mbti_compatibility(mbti1, mbti2):
    """
    分析两个MBTI类型的匹配度
    
    参数:
        mbti1: 第一个MBTI类型
        mbti2: 第二个MBTI类型
    
    返回:
        匹配度分析字典
    """
    if mbti1 not in MBTI_COMPATIBILITY:
        return None
    
    compatibility_data = MBTI_COMPATIBILITY[mbti1]
    
    result = {
        "mbti1": mbti1,
        "mbti2": mbti2,
        "情感匹配": {"level": "一般", "score": 50, "description": ""},
        "生活匹配": {"level": "一般", "score": 50, "description": ""},
        "事业匹配": {"level": "一般", "score": 50, "description": ""},
        "综合匹配": {"score": 50, "level": "一般", "description": ""}
    }
    
    # 分析各个维度的匹配度
    for dimension in ["情感匹配", "生活匹配", "事业匹配"]:
        dimension_data = compatibility_data.get(dimension, {})
        level = "一般"
        
        for match_level, mbtis in dimension_data.items():
            if mbti2 in mbtis:
                level = match_level
                break
        
        score = get_compatibility_score(level)
        result[dimension] = {
            "level": level,
            "score": score,
            "description": f"{mbti1}与{mbti2}在{dimension}方面匹配度为{level}（{score}分）"
        }
    
    # 计算综合匹配度
    total_score = (
        result["情感匹配"]["score"] +
        result["生活匹配"]["score"] +
        result["事业匹配"]["score"]
    ) / 3
    
    if total_score >= 85:
        overall_level = "极佳"
    elif total_score >= 70:
        overall_level = "良好"
    elif total_score >= 50:
        overall_level = "一般"
    else:
        overall_level = "较差"
    
    result["综合匹配"] = {
        "score": int(total_score),
        "level": overall_level,
        "description": f"{mbti1}与{mbti2}的综合匹配度为{overall_level}（{int(total_score)}分）"
    }
    
    return result


def analyze_combined_compatibility(zodiac1, mbti1, zodiac2, mbti2):
    """
    综合分析星座和MBTI的匹配度
    
    参数:
        zodiac1: 第一个星座
        mbti1: 第一个MBTI类型
        zodiac2: 第二个星座
        mbti2: 第二个MBTI类型
    
    返回:
        综合匹配度分析字典
    """
    zodiac_result = analyze_zodiac_compatibility(zodiac1, zodiac2)
    mbti_result = analyze_mbti_compatibility(mbti1, mbti2)
    
    if not zodiac_result or not mbti_result:
        return None
    
    # 计算综合匹配度（星座和MBTI各占50%权重）
    combined_result = {
        "zodiac_analysis": zodiac_result,
        "mbti_analysis": mbti_result,
        "情感匹配": {
            "score": int((zodiac_result["情感匹配"]["score"] + mbti_result["情感匹配"]["score"]) / 2),
            "level": "",
            "description": ""
        },
        "生活匹配": {
            "score": int((zodiac_result["生活匹配"]["score"] + mbti_result["生活匹配"]["score"]) / 2),
            "level": "",
            "description": ""
        },
        "事业匹配": {
            "score": int((zodiac_result["事业匹配"]["score"] + mbti_result["事业匹配"]["score"]) / 2),
            "level": "",
            "description": ""
        },
        "综合匹配": {
            "score": 0,
            "level": "",
            "description": ""
        }
    }
    
    # 确定匹配度等级
    for dimension in ["情感匹配", "生活匹配", "事业匹配"]:
        score = combined_result[dimension]["score"]
        if score >= 85:
            level = "极佳"
        elif score >= 70:
            level = "良好"
        elif score >= 50:
            level = "一般"
        else:
            level = "较差"
        
        combined_result[dimension]["level"] = level
        combined_result[dimension]["description"] = f"综合{dimension}匹配度为{level}（{score}分）"
    
    # 计算综合匹配度
    total_score = (
        combined_result["情感匹配"]["score"] +
        combined_result["生活匹配"]["score"] +
        combined_result["事业匹配"]["score"]
    ) / 3
    
    if total_score >= 85:
        overall_level = "极佳"
    elif total_score >= 70:
        overall_level = "良好"
    elif total_score >= 50:
        overall_level = "一般"
    else:
        overall_level = "较差"
    
    combined_result["综合匹配"] = {
        "score": int(total_score),
        "level": overall_level,
        "description": f"综合匹配度为{overall_level}（{int(total_score)}分）"
    }
    
    return combined_result


def format_compatibility_analysis(compatibility_result, analysis_type="combined"):
    """
    格式化匹配度分析结果
    
    参数:
        compatibility_result: 匹配度分析结果
        analysis_type: 分析类型 ("zodiac", "mbti", "combined")
    
    返回:
        格式化的字符串
    """
    if not compatibility_result:
        return "无法分析匹配度"
    
    result = "【匹配度分析】\n\n"
    
    if analysis_type == "combined":
        result += f"━━━ 星座匹配分析 ━━━\n"
        zodiac_analysis = compatibility_result.get("zodiac_analysis", {})
        result += f"情感匹配：{zodiac_analysis.get('情感匹配', {}).get('level', '一般')}（{zodiac_analysis.get('情感匹配', {}).get('score', 50)}分）\n"
        result += f"生活匹配：{zodiac_analysis.get('生活匹配', {}).get('level', '一般')}（{zodiac_analysis.get('生活匹配', {}).get('score', 50)}分）\n"
        result += f"事业匹配：{zodiac_analysis.get('事业匹配', {}).get('level', '一般')}（{zodiac_analysis.get('事业匹配', {}).get('score', 50)}分）\n"
        result += f"综合匹配：{zodiac_analysis.get('综合匹配', {}).get('level', '一般')}（{zodiac_analysis.get('综合匹配', {}).get('score', 50)}分）\n\n"
        
        result += f"━━━ MBTI匹配分析 ━━━\n"
        mbti_analysis = compatibility_result.get("mbti_analysis", {})
        result += f"情感匹配：{mbti_analysis.get('情感匹配', {}).get('level', '一般')}（{mbti_analysis.get('情感匹配', {}).get('score', 50)}分）\n"
        result += f"生活匹配：{mbti_analysis.get('生活匹配', {}).get('level', '一般')}（{mbti_analysis.get('生活匹配', {}).get('score', 50)}分）\n"
        result += f"事业匹配：{mbti_analysis.get('事业匹配', {}).get('level', '一般')}（{mbti_analysis.get('事业匹配', {}).get('score', 50)}分）\n"
        result += f"综合匹配：{mbti_analysis.get('综合匹配', {}).get('level', '一般')}（{mbti_analysis.get('综合匹配', {}).get('score', 50)}分）\n\n"
        
        result += f"━━━ 综合匹配分析 ━━━\n"
        result += f"情感匹配：{compatibility_result.get('情感匹配', {}).get('level', '一般')}（{compatibility_result.get('情感匹配', {}).get('score', 50)}分）\n"
        result += f"生活匹配：{compatibility_result.get('生活匹配', {}).get('level', '一般')}（{compatibility_result.get('生活匹配', {}).get('score', 50)}分）\n"
        result += f"事业匹配：{compatibility_result.get('事业匹配', {}).get('level', '一般')}（{compatibility_result.get('事业匹配', {}).get('score', 50)}分）\n"
        result += f"综合匹配：{compatibility_result.get('综合匹配', {}).get('level', '一般')}（{compatibility_result.get('综合匹配', {}).get('score', 50)}分）\n\n"
    else:
        result += f"情感匹配：{compatibility_result.get('情感匹配', {}).get('level', '一般')}（{compatibility_result.get('情感匹配', {}).get('score', 50)}分）\n"
        result += f"生活匹配：{compatibility_result.get('生活匹配', {}).get('level', '一般')}（{compatibility_result.get('生活匹配', {}).get('score', 50)}分）\n"
        result += f"事业匹配：{compatibility_result.get('事业匹配', {}).get('level', '一般')}（{compatibility_result.get('事业匹配', {}).get('score', 50)}分）\n"
        result += f"综合匹配：{compatibility_result.get('综合匹配', {}).get('level', '一般')}（{compatibility_result.get('综合匹配', {}).get('score', 50)}分）\n\n"
    
    return result

