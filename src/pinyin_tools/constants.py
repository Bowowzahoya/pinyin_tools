PINYIN_ALPHABET = "abcdefghijklmnopqrstuüwxyz' "
PINYIN_ALPHABET_EXTENDED = PINYIN_ALPHABET+"v-" # extended with common alternative writing
PINYIN_ALPHABET_WITH_TONES = PINYIN_ALPHABET+'éèēěáàāǎúùūǔǘǜǖǚíìīǐóòōǒ'
PINYIN_ALPHABET_WITH_TONES_EXTENDED = PINYIN_ALPHABET_EXTENDED+'éèēěáàāǎúùūǔǘǜǖǚíìīǐóòōǒŭӑӗĭ'

ALLOWED_SYLLABLES = ["ba","bo","bai","bei","bao","ban","ben","bang","beng","bi",\
    "biao","bie","bian","bin","bing","bu",\
    "pa","po","pai","pei","pao","pou","pan","pen","pang","peng","pi",\
    "piao","pie","pian","pin","ping","pu",\
    "ma","mo", "me","mai","mei","mao","mou","man","men","mang","meng",\
    "mi","miao","mie","miu","mian","min","ming","mu",\
    "fa","fo","fei","fou","fan","fen","fang","feng","fu",\
    "da","de","dai","dei","dou","dao","dan","den","dang","deng",\
    "dong","di","dia","diao","die","diu","dian","ding","du","duo",\
    "dui","duan","dun",\
    "ta","te","tai","tei","tou","tao","tan","tang","teng","tong","ti",\
    "tiao", "tie","tian","ting","tu","tuo","tui","tuan","tun",\
    "na","ne","nai","nei","nou","nao","nan","nen","nang","neng",\
    "nong","ni","niao", "nie","niu","nian","nin","niang","ning","nu",\
    "nuo","nuan","nun","nü","nüe",\
    "la","lo","le","lai","lei","lou","lao","lan","lang","leng","long",\
    "li","lia","liao", "lie","liu","lian","lin","liang","ling","lu",\
    "luo","luan","lun","lü","lüe",\
    "ga","ge","gai","gei","gou","gao","gan","gen","gang","geng",\
    "gong",\
    "gu","gua","guo","guai","gui","guan","gun","guang",\
    "ka","ke","kai","kei","kou","kao","kan","ken","kang","keng",\
    "kong",\
    "ku","kua","kuo","kuai","kui","kuan","kun","kuang",\
    "ha","he","hai","hei","hou","hao","han","hen","hang","heng",\
    "hong","hu","hua","huo","huai","hui","huan","hun","huang",\
    "sa","se","si","sai","sou","sao","san","sen","sang","seng","song",\
    "su","suo","sui","suan","sun",\
    "za","ze","zi","zai","zei","zou","zao","zan","zen","zang","zeng",\
    "zong","zu","zuo","zui","zuan","zun",\
    "ca","ce","ci","cai","cou","cao","can","cen","cang","ceng","cong",\
    "cu","cuo","cui","cuan","cun",\
    "re","ri","rou","rao","ran","ren","rang","reng","rong",\
    "ru","rua","ruo","rui","ruan","run",\
    "sha","she","shi","shai","shei","shou","shao","shan","shen",\
    "shang","sheng","shu","shua","shuo","shuai","shui","shuan","shun",\
    "shuang",\
    "zha","zhe","zhi","zhai","zhei","zhou","zhao","zhan","zhen",\
    "zhang","zheng","zhong","zhu","zhua","zhuo","zhuai","zhui",\
    "zhuan","zhun","zhuang",\
    "cha","che","chi","chai","chou","chao","chan","chen","chang",\
    "cheng","chong","chu","chua","chuo","chuai","chui","chuan","chun",\
    "chuang",\
    "xi","xia","xiao","xie","xiu","xian","xin","xiang","xing","xiong",\
    "xu","xue","xuan","xun",\
    "ji","jia","jiao","jie","jiu","jian","jin","jiang","jing","jiong",\
    "ju","jue","juan","jun",\
    "qi","qia","qiao","qie","qiu","qian","qin","qiang","qing","qiong",\
    "qu","que","quan","qun",\
    "wu","wa","wo","wai","wei","wan","wang","wen","weng",\
    "yo","you","yi","ya","yao","ye","yan","yin","yang","ying","yong",\
    "yu","yue","yuan","yun",\
    "a","o","e","ai","ei","ou","ao","an","en","ang","eng","er"]

# Extended with some common alternative writings
ALLOWED_SYLLABLES_EXTENDED = ALLOWED_SYLLABLES + \
    ["lyu", "lyue", "nyu", "nyue", \
    "lue", "nue", \
    "lv", "lve", "nv", "nve", \
    "shaan"] # from shaanxi

TONES_DICTIONARY = {'e':'éèēě',\
        'a':'áàāǎ',\
        'u':'úùūǔ',\
        'ü':'ǘǜǖǚ',\
        'v':'v',\
        'i':'íìīǐ',\
        'o':'óòōǒ'}

TONES_DICTIONARY_EXTENDED = {'e':'éèēěӗ',\
        'a':'áàāǎӑ',\
        'u':'úùūǔŭ',\
        'ü':'ǘǜǖǚ',\
        'i':'íìīǐĭ',\
        'o':'óòōǒŏ'}

TONE_LOCATION_FOR_COMPOUND_VOWELS = {'ai':0, 'ao':0,\
        'ei':0,\
        'ia':1,'iao':1,'ie':1,'io':1,'iu':1,\
        'ou':0,\
        'ua':1,'ue':1,'uai':1,'ui':1,'uo':1,\
        'üe':1,'ve':1}

def get_allowed_syllables_with_tones(allowed_syllables, tone_dictionary=TONES_DICTIONARY):
    allowed_syllables_with_tones = allowed_syllables.copy()
    
    def strip_to_vowels(s):
        for c in 'bcdfghjklmnpqrstwxyz':
            s = s.replace(c,'')
        return s
    
    for syl in allowed_syllables:
        vowels = strip_to_vowels(syl)

        if vowels in TONE_LOCATION_FOR_COMPOUND_VOWELS.keys():
            letter = vowels[TONE_LOCATION_FOR_COMPOUND_VOWELS[vowels]]
        else:
            letter = vowels
        
        for letter_with_tone in TONES_DICTIONARY[letter]:
            allowed_syllables_with_tones += [syl.replace(letter, letter_with_tone)]
    return allowed_syllables_with_tones      

ALLOWED_SYLLABLES_WITH_TONES = get_allowed_syllables_with_tones(ALLOWED_SYLLABLES)

allowed_syllables_extended_trimmed = ALLOWED_SYLLABLES_EXTENDED[:-1] # don't include 'shaan' because never spelled with tones
ALLOWED_SYLLABLES_WITH_TONES_EXTENDED = get_allowed_syllables_with_tones(allowed_syllables_extended_trimmed, tone_dictionary=TONES_DICTIONARY_EXTENDED)

DELIMITERS_PATTERN = "'| "
DELIMITERS_EXTENDED_PATTERN = "'| |-"

TWO_HANZI_FAMILY_NAMES = [('si', 'ma'), ('ou', 'yang'), ('shang', 'guan'), 
    ('si', 'tu'), ('zhu', 'ge'), ('xia', 'hou'), ('huang', 'fu'), ('hu', 'yan')]
NAME_LENGTH_POSSIBILITIES = [2, 3, 4]

from numpy import nan as npnan
NAN_VALUES = ["", npnan, None]
INTERPUNCTION_CHARACTERS = ".,-:;'?!()"+'"'

NORMAL_MODE = "normal"
EXTENDED_MODE = "extended"
LAZY_MODE = "lazy"
TONES_MODE = "tones"
TONES_EXTENDED_MODE = "tones_extended"