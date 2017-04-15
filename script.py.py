import re, os

er = ["Ъ", "ъ"]
fita = ["Ѳ", "ѳ"]
yat = ["Ѣ", "ѣ"]
ij = ["Ѵ", "ѵ"]
i10 = ["І", "і"]

vowels = "уеыаоэюияёйУЕЫАОЭЯИЮЁЙ"
other = "ьЬъЪЙй"
consonants = "цкнгшщзхфвпрлджчсмтьбЦКНГШЩЗХФВПРЛДЖЧСМТЬБ"
fita_words = ["агаѳья", "анѳимъ", "аѳанасій", "аѳина", "варѳоломей", "голіаѳъ", "дороѳей", "евѳимій",
              "ероѳей", "марѳа", "матѳей", "меѳодій", "наѳанаилъ", "парѳенонъ", "пиѳагоръ", "руѳь", "саваоѳъ",
              "тимоѳей", "эсѳирь", "іудиѳь", "ѳаддей", "ѳекла", "ѳемида", "ѳемистоклъ", "ѳеодоръ", "ѳёдоръ", "ѳедя",
              "ѳеодосій", "ѳедосій", "ѳеодосія", "ѳеодотъ", "ѳедотъ", "ѳеофанъ", "ѳеофилъ", "ѳерапонтъ", "ѳома", "ѳоминична",
              "аѳины", "аѳонъ", "виѳанія", "виѳезда", "виѳинія", "виѳлеемъ", "виѳсаида", "геѳсиманія", "голгоѳа", "карѳагенъ",
              "коринѳъ", "мараѳонъ", "парѳія", "парѳенонъ", "эѳіопія", "ѳаворъ", "ѳеодосія", "ѳермофилы", "ѳессалія", "ѳессалоники",
              "ѳивы", "ѳракія", "коринѳяне", "парѳяне", "скиѳы", "эѳіопы", "ѳиване", "анаѳема", "акаѳистъ", "апоѳеозъ", "апоѳегма", "ариѳметика",
              "диѳирамбъ", "еѳимоны", "каѳолическій", "каѳедра", "каѳизма", "киѳара", "левіаѳанъ", "логариѳмъ", "мараѳонъ", "миѳъ",
              "миѳологія", "моноѳелитство", "орѳографія", "орѳоэпія", "паѳосъ", "риѳма", "эѳиръ", "ѳиміамъ", "ѳита"]
ij_words = ["мѵро", "сѵнодъ", "ѵпостась"]

yat_roots = ['великолѣпный', 'человѣческій', 'десятилѣтіе', 'двѣнадцатый', 'послѣдствіе', 'сомнѣваться',
             'запечатлѣнъ', 'выслѣживать', 'просвѣщеніе', 'замѣститель', 'застѣнчивый', 'равновѣсіе', 'сильнѣйшій',
             'отнѣкаться', 'примѣчаніе', 'высмѣивать', 'наслѣдство', 'двѣнадцать', 'взбѣситься', 'нѣкоторыхъ',
             'надѣвывалъ', 'издѣваться', 'намѣстникъ', 'праведникъ', 'свирѣпѣетъ', 'богадѣльнѣ', 'исповѣдать',
             'разсѣянный', 'изобрѣтать', 'непремѣнно', 'встрѣтить', 'нѣжинскій', 'сильнѣйше', 'свидѣтель',
             'приобрѣлъ', 'лѣкарство', 'насѣкомое', 'оцѣпенѣть', 'измѣнникъ', 'намѣреніе', 'слѣдствіе', 'сосѣдствѣ',
             'поколѣніе', 'надѣяться', 'содѣянный', 'напримѣръ', 'нѣкоторый', 'застѣнокъ', 'убѣжденіе', 'свѣ́дѣніе',
             'подсѣкать', 'нѣсколько', 'встрѣчать', 'пообѣдалъ', 'кромѣшный', 'пѣстовать', 'крѣпиться', 'вѣстовать',
             'затѣйникъ', 'похѣрить', 'обвѣщать', 'посѣщать', 'выѣзжать', 'цѣхановъ', 'выдѣлять', 'смѣяться', 'бѣженецъ',
             'вѣжливый', 'побѣдить', 'стѣснять', 'свѣтлана', 'свѣтёлка', 'лицемѣръ', 'надѣванъ', 'загнѣдка', 'освѣжать',
             'печенѣгъ', 'медвѣдка', 'помѣщикъ', 'смотрѣть', 'поспѣшно', 'внѣдрить', 'надѣвать', 'замѣчать', 'застрѣха',
             'желѣзный', 'цвѣтенье', 'обрѣтать', 'человѣка', 'вѣроятно', 'загнѣтка', 'телѣжный', 'посѣтить', 'крѣпость',
             'цѣженный', 'мѣщанинъ', 'краснѣть', 'расцвѣлъ', 'обмѣнять', 'смѣщеніе', 'стрѣлять', 'увѣчнымъ', 'грѣшникъ',
             'плѣнникъ', 'вѣ́дѣніе', 'калѣчить', 'зѣвывалъ', 'срѣтеніе', 'свирѣпый', 'лѣстница', 'нѣжиться', 'нынѣшній',
             'исцѣлять', 'извѣстно', 'внѣдрять', 'печенѣги', 'цѣловать', 'подгнѣта', 'суевѣріе', 'сѣтовать', 'надѣлать',
             'цѣлиться', 'человѣкъ', 'побѣдила', 'сомнѣніе', 'дѣйствіе', 'орѣшникъ', 'застѣнок', 'рогнѣда', 'прорѣха',
             'рѣшетка', 'индѣйцы', 'совѣсть', 'сосѣдка', 'снѣжный', 'бѣшеный', 'опѣшить', 'хрѣномъ', 'рѣдькой', 'одѣяніе',
             'обрѣсти', 'одѣвать', 'счастьѣ', 'дѣтскій', 'индѣецъ', 'вдвойнѣ', 'грѣшный', 'прѣсный', 'рѣшётка', 'дѣвочка',
             'спѣшить', 'поцѣлуй', 'предѣлъ', 'смѣтить', 'голѣмый', 'примѣръ', 'блѣдный', 'помѣтка', 'крѣпкій', 'доспѣхи',
             'лѣнивый', 'цѣвница', 'вѣнчать', 'невѣжда', 'созрѣли', 'сильнѣй', 'болѣйте', 'просѣка', 'издѣвка', 'ротозѣй',
             'созрѣть', 'привѣтъ', 'вдалекѣ', 'днѣстра', 'копѣйка', 'онѣгинъ', 'крѣпокъ', 'дѣйство', 'сильнѣе', 'мѣшкать',
             'цѣплять', 'свирѣль', 'рѣсница', 'промѣнѣ', 'свѣтецъ', 'осѣнять', 'повѣсть', 'нѣкогда', 'плѣнило', 'алексѣй',
             'овѣвать', 'внѣшній', 'сѣченіе', 'обѣщать', 'калѣкой', 'затѣять', 'пѣстунъ', 'свѣжѣть', 'убѣжище', 'плѣнять',
             'медвѣдь', 'нелѣпый', 'убѣжалъ', 'тѣсномъ', 'нарѣчіе', 'увѣчить', 'убѣдить', 'свѣсилъ', 'рѣсницы', 'невѣста',
             'лелѣять', 'днѣстръ', 'вертѣть', 'плѣсень', 'здѣшній', 'вмѣстѣ', 'бесѣда', 'апрѣль', 'полѣно', 'еремѣй', 'отвѣтъ',
             'лѣпить', 'обрѣлъ', 'мнѣніе', 'дѣлать', 'вѣники', 'тѣсный', 'вѣнецъ', 'зѣвать', 'двѣсти', 'прѣлый', 'бѣлуга', 'вѣтеръ',
             'телѣга', 'вѣщать', 'нѣмецъ', 'зрѣлый', 'нѣжить', 'ѣздить', 'лѣвѣть', 'вѣникъ', 'лѣшимъ', 'пѣвецъ', 'мѣсяцъ', 'бѣлена',
             'вѣнокъ', 'дѣлить', 'лѣтній', 'мѣсить', 'завѣтъ', 'помѣха', 'бѣдный', 'сѣвера', 'гнѣвно', 'хотѣть', 'прѣніе', 'доселѣ',
             'мѣшать', 'стрѣха', 'свѣжій', 'лѣсной', 'мѣтить', 'пѣтухъ', 'тяжелѣ', 'лѣкарь', 'отколѣ', 'вѣшать', 'нѣманъ', 'сѣдѣть',
             'пѣнязь', 'цѣдить', 'зѣницы', 'недѣля', 'вѣдать', 'дѣлитъ', 'нелѣпо', 'побѣда', 'однѣхъ', 'гнѣздо', 'вѣчный', 'рѣчной',
             'рѣжетъ', 'замѣшу', 'елисѣй', 'болѣть', 'дѣвать', 'вдѣжка', 'рѣшить', 'рѣзать', 'ѣйшій$', 'зрѣніе', 'рѣшать', 'тѣшить',
             'рѣшето', 'пѣхота', 'оцѣнка', 'гнѣзда', 'навѣсъ', 'стрѣла', 'крѣпко', 'апрѣлѣ', 'колѣно', 'мѣнять', 'слѣпой', 'матвѣй',
             'доколѣ', 'лѣчить', 'желѣзо', 'вмѣсто', 'смыслѣ', 'днѣпръ', 'зѣница', 'смѣлый', 'бѣгалъ', 'мѣшокъ', 'обвѣтъ', 'гнѣзно',
             'одѣяло', 'сѣверъ', 'рѣпица', 'калѣка', 'совѣтъ', 'днѣпра', 'кѣльцы', 'смѣтка', 'посѣвъ', 'сергѣй', 'бѣльмо', 'цвѣсти',
             'отселѣ', 'клѣтка', 'рѣдька', 'повѣса', 'звѣзда', 'успѣхъ', 'нѣжный', 'рѣдьку', 'ѣющій$', 'ѣвшій$', 'вѣдьма', 'звѣзды',
             'мѣдный', 'смѣетъ', 'мѣрило', 'рѣдкій', 'гнѣдой', 'сосѣдъ', 'рѣзвый', 'плѣнъ', 'нѣдра', 'хлѣбъ', 'вѣщій', 'свѣча', 'онѣга',
             'вѣтка', 'затѣя', 'вездѣ', 'спѣть', 'нѣкій', 'кромѣ', 'пѣсня', 'вѣять', 'сѣдой', 'вѣшка', 'лѣшій', 'орѣхъ', 'смѣхъ', 'рѣчка',
             'вѣтвь', 'бѣдны', 'послѣ', 'возлѣ', 'всѣмъ', 'свѣтъ', 'имѣть', 'сѣять', 'вѣтки', 'бѣлый', 'сѣдла', 'плѣшь', 'стѣна', 'подлѣ',
             'лѣвый', 'обѣдъ', 'гнѣвъ', 'цѣвьё', 'мнѣти', 'грѣхъ', 'спѣхъ', 'мѣсто', 'звѣрь', 'пѣгій', 'хрѣнъ', 'одѣть', 'извнѣ', 'развѣ',
             'орѣхи', 'цвѣла', 'слѣпъ', 'рѣдко', 'цвѣтъ', 'сѣрый', 'цѣлый', 'обѣтъ', 'нѣмой', 'млѣть', 'бѣлье', 'лѣзть', 'нѣкто', 'тѣсто',
             'умѣлъ', 'сѣдло', 'цѣвье', 'зѣнки', 'вѣжды', 'ѣхать', 'вѣеръ', 'пѣшій', 'цвѣты', 'вѣсть', 'бѣлка', 'ѣніе$', 'вѣсти', 'вѣрно',
             'спѣлъ', 'смѣть', 'столѣ', 'клѣть', 'вродѣ', 'зрѣть', 'сѣтка', 'здѣсь', 'смѣта', 'обѣих', 'школѣ', 'всѣхъ', 'нѣчто', 'слѣдъ',
             'плѣна', 'лѣха́', 'смѣсь', 'числѣ', 'рѣшка', 'цѣвка', 'нѣкiй', 'нѣмцы', 'вѣдай', 'снѣгъ', 'цвѣлъ', 'утѣха', 'глѣбъ', 'словѣ',
             'мѣтко', 'сѣсть', 'хлѣвъ', 'прѣть', 'рѣять', 'стрѣл', 'хлѣб', 'лѣто', 'мѣна', 'мѣдь', 'цвѣч', 'хѣръ', 'индѣ', 'сѣнь', 'сѣра',
             'пѣть', 'змѣй', 'бѣдъ', 'вѣче', 'сѣмя', 'вѣкъ', 'мѣра', 'рѣже', 'вѣра', 'мѣхъ', 'рѣпу', 'тѣло', 'вѣна', 'лѣха', 'лѣнь', 'менѣ',
             'ѣсть', 'бѣсы', 'лѣсу', 'нѣга', 'морѣ', 'вѣки', 'зѣло', 'сѣлъ', 'цѣпъ', 'себѣ', 'свѣч', 'цѣпи', 'дѣва', 'цѣпь', 'сѣку', 'нѣтъ',
             'вѣко', 'сѣча', 'бѣда', 'однѣ', 'нынѣ', 'тѣнь', 'пѣна', 'свѣт', 'вѣжа', 'цвѣт', 'бѣсъ', 'цѣлъ', 'сѣть', '^внѣ', 'нѣмъ', 'смѣх',
             'рѣпа', 'тѣмъ', 'снѣг', 'кѣмъ', 'мѣлъ', 'рѣки', 'вѣха', 'лѣсъ', 'рѣчь', 'дѣти', 'рѣка', 'дѣло', 'дѣть', 'дѣдъ', 'вѣнѣ', 'вѣди',
             'гнѣв', 'сѣни', 'тебѣ', 'зѣвъ', '^далѣ', 'ѣть$', 'змѣя', 'сѣно', 'чѣмъ', 'цѣль', 'грѣх', 'ѣлъ$', 'болѣ', 'цѣна', 'вѣно', 'сѣчь',
             'сѣвъ', 'бѣгъ', 'вѣст', 'вѣсъ', 'свѣж', 'бѣса', '^онѣ$', 'ѣю$', '^всѣ$', '^гдѣ$', '^ѣла$', 'вѣд', '^двѣ$', 'ѣя$', 'вѣж', '^ѣда', 'обѣ',
             '^мнѣ$', '^внѣ$', '^ѣду', '^ѣлъ', "^ѣд", "^ѣм", "^ѣс", "^ѣж", "^ѣх", "^ѣз"]


def create_yat_roots_data(roots_list, replacer):
    res = []
    for i in roots_list:
        word = re.sub(yat[1], replacer, i)
        if len(word) > 3 and word[-1] in vowels:
            word = word[:-1] + "..?"
        res.append(word)
    return res
yat_roots_marks = create_yat_roots_data(yat_roots, "[Ъъ]")


def create_letter_data(words_list, letters):
    res = []
    for i in words_list:
        if i[0] == letters[1]:
            res.append("^." + i[1:-1] + ".+$")
        elif i[-1] == letters[1]:
            res.append("^" + i[:-1] + ".$")
        else:
            parts = i.split(letters[1])
            res.append("^" + parts[0] + "." + parts[1][:-1] + ".+$")
    return res

fita_marks = create_letter_data(fita_words, fita)
ij_marks = create_letter_data(ij_words, ij)

def check_i10(word):
    letters = re.findall("[iIl1]", word)
    if letters:
        #print(word)
        for letter in set(letters):
            if letter == "I":
                parts = word.split("I")
                res = parts[0]
                if len(parts) > 1:
                    for i in range(len(parts)):
                        if i > 0:
                            if parts[i] and re.search(parts[i][0], vowels) or (parts[0].lower() == "м" and parts[1].lower() == "ръ"):
                                res += (i10[0] + parts[i])
                            else:
                                res += ("I" + parts[i])
                word = res
                                
            elif letter == "i":
                parts = word.split("i")
                res = parts[0]
                if len(parts) > 1:
                    for i in range(len(parts)):
                        if i > 0:
                            if parts[i] and re.search(parts[i][0], vowels) or (parts[0].lower() == "м" and parts[1].lower() == "ръ"):
                                res += (i10[1] + parts[i])
                            else:
                                res += ("i" + parts[i])
                word = res
            elif letter == "l":
                parts = word.split("l")
                res = parts[0]
                if len(parts) > 1:
                    for i in range(len(parts)):
                        if i > 0:
                            if parts[i] and re.search(parts[i][0], vowels) or (parts[0].lower() == "м" and parts[1].lower() == "ръ"):
                                res += (i10[1] + parts[i])
                            else:
                                res += ("l" + parts[i])
                word = res
            elif letter == "1":
                parts = word.split("1")
                res = parts[0]
                if len(parts) > 1:
                    for i in range(len(parts)):
                        if i > 0:
                            if  parts[i] and re.search(parts[i][0], vowels) or (parts[0].lower() == "м" and parts[1].lower() == "ръ"):
                                res += (i10[1] + parts[i])
                            else:
                                res += ("1" + parts[i])
                word = res
        return word
    return word

ij_marks = ["^м.р.+$", "^с.нод.+$", "^.постас.+$"]
def check_ij (word):
    upper = re.findall("[VYУ]", word)
    lower = re.findall("[vyу]", word)
    low_word = word.lower()
    if upper or lower:
        for i in ij_marks:
            if re.search(i, low_word) and (word[-1] in vowels or word[-1] in other):
                parts = i[1:-1].split(".")
                res = ""
                case = ""
                if upper:
                    case = ij[0]
                elif lower:
                    case = ij[1]
                if parts[0]:
                    res = parts[0]
                    res += case
                else:
                    res = case
                res += parts[1]
                res += word[-1]
                return res
    return word

def check_fita (word):
    upper = re.findall("[ОO]", word)
    lower = re.findall("[оo08]", word)
    low_word = word.lower()
    if upper or lower:
        for i in fita_marks:
            if re.search(i, low_word) and (word[-1] in vowels or word[-1] in other):
                parts = i[1:-1].split(".")
                res = ""
                case = ""
                if upper:
                    case = fita[0]
                elif lower:
                    case = fita[1]
                if parts[0]:
                    res = parts[0]
                    res += case
                else:
                    res = case
                res += parts[1]
                res += word[-1]
                return res
    return word


#ьЬъЪ
def check_yat (word):
    upper = re.search("[Ъ]", word)
    lower = re.search("[ъ]", word)
    low_word = word.lower()
    if upper or lower:
        for i in yat_roots_marks:
            if re.search(i, low_word):
                if upper:
                    return remask_word(word, i, "upper")
                elif lower:
                    return remask_word(word, i, "lower")        
    return word

def remask_word(word, mask, case = "lower"):
    repl_mask = ""
    if mask[-3:] == "..?":
        repl_mask = mask[:-3]
    else:
        repl_mask = mask
    if case == "upper":
        case = yat[0]
    else:
        case = yat[1]
    correct_mask = re.sub("\[Ъъ\]", case, repl_mask)
    word = re.sub(repl_mask, correct_mask, word)
    word = re.sub("[\^\$]", "", word)
    return word
    
def change_dir(path = ""):
    for i in os.walk(path):
        if i[2]:
            for j in i[2]:
                file_path = i[0] + "\\" + j
                file_result = ""
                try:
                    a = open(file_path, "r", encoding="utf-8")
                    for k in a:
                        string_result = ""
                        parts = k.split()
                        if int(parts[2]) < 1918:
                            word1_parts = parts[0].split("_")
                            if len(word1_parts[0]) > 1:
                                word1_parts[0] = check_yat(word1_parts[0])
                                word1_parts[0] = check_ij(word1_parts[0])
                                word1_parts[0] = check_fita(word1_parts[0])
                                word1_parts[0] = check_i10(word1_parts[0])
                            word1 = "_".join(word1_parts)
			
                            word2_parts = parts[1].split("_")
                            if len(word2_parts[0]) > 1:
                                word2_parts[0] = check_yat(word2_parts[0])
                                word2_parts[0] = check_ij(word2_parts[0])
                                word2_parts[0] = check_fita(word2_parts[0])
                                word2_parts[0] = check_i10(word2_parts[0])
                            word2 = "_".join(word2_parts)

                            string_result = "\t".join([word1, word2, parts[2], parts[3], parts[4]])
                            string_result += "\n"
                            file_result += string_result
                    a.close()
                    a = open("F:\\Projects\\test_res" + "\\" + j + "_checked", "w", encoding="utf-8")
                    a.write(file_result)
                    a.close()
                    print("File finished")
                except:
                    print("Проблема с файлом:", file_path)
change_dir("F:\\Projects\\test")
