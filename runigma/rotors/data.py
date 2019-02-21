# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of Py-Enigma, the Enigma Machine simulation.
# Py-Enigma is released under the MIT License (see License.txt).

"""data.py - This file contains rotor & reflector data for all the types
we simulate.

"""

# This data is taken from Dirk Rijmenants very informative and useful Enigma
# website: "Techical Details of the Engigma Machine"
# http://users.telenet.be/d.rijmenants/en/enigmatech.htm
#
# Rotors I-V were used by the Heer, Luftwaffe, and Kriegsmarine. The
# Kriegsmarine added rotors VI-VIII to the M3 model, and added Beta & Gamma to
# the M4 model (used with thin reflectors only). Note that Beta & Gamma rotors
# did not rotate.
#
# The Heer, Luftwaffe, & Kriegsmarine M3 machines used reflectors B & C,
# while the Kriegsmarine M4 used thin reflectors B & C.
#

ROTORS = {
    'А': {
        'wiring': 'Сu6ЩАЧzХcw2nt5jhОЦБКxГУЛЖlЪ_Д0ТdiИ9fo4rgs1ФkНРq8vЕШaemПЫЬВ3yb7ЗЮpЭЁМЯЙ',
        'stepping': 'Р5n',
    },
    'Б': {
        'wiring': 'nГАНЧm1ЕaydПРОЛosМЙqЫ6СВ_jvХ7cБixЬ8ФtИЪwЦЗ2eУkb9rhКЖД45ugЁ0ЮЭpfТЩ3zlЯШ',
        'stepping': 'gcv',
    },
    'В': {
        'wiring': '9ШxКyjЙВМХЭnmДit3ЬЛЩЧЯСФЖsu2БqzЫoПЮl8kНe0Е4Ъc7whА1vОЦИГУ6dagrТ_fЁ5bРpЗ',
        'stepping': 'ЧmЫ',
    },
    'Г': {
        'wiring': 'sБЪРНДЖbП6ЭrУpvАdiЧХЮЗЬaШ9ЛВЙ8Т5ЦtИГ04МexqЫc1_7ЕКzОgufwkЩЯ2ЁoСmjФ3yhln',
        'stepping': 'cЕЩ',
    },
    'Д': {
        'wiring': 'hЙa9КЛРcmpvПТ67oГВ4ШБ3f_ИЁ1М0ОЪЯСydНУ2АxzjЕ8ЭЫХewЩiЖЗtubЬДЦЮkqns5gЧФrl',
        'stepping': 'cХv',
    },
    'Е': {
        'wiring': 'ЯwТrgЖЙ5СxЭЧГczОhЫnА4dЛ1ubЪРКВeНЗПyФlp2Е3960sМЁvДoamБfЮ8Ь7jЦiqХУЩktИ_Ш',
        'stepping': 'ЪО0',
    },
    'Ё': {
        'wiring': 'ГР20Е3fЫСЦО9АШМЭ6oПaqКЬctyЛЩnЮhЁЯНИЧ4xzДj8_ФbslУВdrТ5Б7k1mЖeХvuwЗiЙgЪp',
        'stepping': 'axВ',
    },
    'Ж': {
        'wiring': 'СПФУБ4_МКЕj6ЁОkctЖЮЛohВ93ЬqЪyЙ5bmНr1ДЫЧЯ7ГewЦ8РШТaugАf0dpИЭs2ЩznlvХiЗx',
        'stepping': 'aМЯ',
    },
    'З': {
        'wiring': 'xЫПСКtehЁИcuaФЧЮn0zyvЛ_Ц6ЭОiГpШ8МБoР71jsbХДq23АЖfwТВЩgЯЬrm9З5ЙЪlУkdЕН4',
        'stepping': 'swЩ',
    },
    'И': {
        'wiring': 'al_bЭСЮ9m0ЛЦuqkЬЖЁoe4Мn7xsУcРgwj6tТvЙ2ЗГhШzf8ЫКЧyИДiВП5rОХd1ЯpНЪЕЩ3БФА',
        'stepping': '8Шd',
    },
    'Й': {
        'wiring': 'П9ТeСШАtЩЕ_ИД3lЗОЧЬ5zcЙpГ2yЭЮЪxЛФiВrЦЁ6ЯsУhЫ8МgjБРКvqХmb4fН71Жua0nwkdo',
        'stepping': 'gСТ',
    },
    'К': {
        'wiring': 'jy2atЪШ4oИ17hМdЙЁЮ698gzrЦЯЧpГcЭkeЗПfmХ5xФЛО0nqБЩНvЕКb_РsiТУЫwlДЬВАЖС3u',
        'stepping': 'aeЫ',
    },
    'Л': {
        'wiring': 'xЮФbsСЧМl2moГЬЭШЫЪПЯ9tНcКqiИА0Уf5БД1ЙjЛr73yОa6eЖzuЁpЩ8ВdЦ_РХ4knТЕhvwЗg',
        'stepping': 'xЬ4',
    },
    'М': {
        'wiring': 'ax9ДЬАОiЫЭ51Я7Ъ_md62ТrФlyПuЖtНЦqЕВБЙcpМЛИГК3kЮ8fsРjogbhe4СШv0zХУwЁЗЧnЩ',
        'stepping': 'cЧУ',
    },
    'Н': {
        'wiring': 'lВИkaС8zЭУЮЧxwЗЫfЩgЯРmqХГ_6ДhcТsy1ЬЦoЕinМНu9ЙФБp5eЪ73b0ПЁЛКvЖАr2jt4dОШ',
        'stepping': 'Лev',
    },
    'О': {
        'wiring': '5qzЕАwukЬ7_tСЙ8Т0КХЪaПБv3ЖbxВШmn1iЧdpИЩgr9ДЮ6hyФlРjНeЯГocs4ЗfУЭО2ЁЛЦЫМ',
        'stepping': '2jУ',
    },
    'П': {
        'wiring': 'ФwegТrnДБЮtИМuВoУЦ6СШХЖЯvl2КЧb4ЫЭyЁО1pАЛdЙГqaЕkЪЗ738Нzxh0Рs9ЩЬ5j_fcПim',
        'stepping': 'ЭТЖ',
    },
    'Р': {
        'wiring': 'mЗ8Р9Т1ДЖФibУ3ОПdМqcВl6enЯИСfrНЧАhaЫpЮwЬЩo7sХ5БjЪygЁЙxvК0ЦukШЛ_zГt4Е2Э',
        'stepping': 'Йs8',
    },
    'С': {
        'wiring': '3y7aibИwВДТЭ_4ЩУЪОФЗ0oЁqn6fjvzeЯЦ5kХsЬЫНШМГСАЖКЙlhЮr1cЧБ9p2РugПtdЛ8xЕm',
        'stepping': 'pbШ',
    },
    'Т': {
        'wiring': 'ЛЫudm2ФЗtjН9ТХПЯГУzЕЙoga_МШnДЩ347iЪbКfЭ5Ёh0ЦpОr6ceЬyЖvsqЧАxРklw1ИЮБВС8',
        'stepping': '6ЪД',
    },
    'У': {
        'wiring': 'З7mАЩk34ФjbН8П1fid6ИgxГТnЫwЁМЧsЬcКЕ_5ЦЙl9vЯzВhРu2ЖeqyСaroЛОЭДУБptХ0ШЮЪ',
        'stepping': 'МЙГ',
    },
    'Ф': {
        'wiring': 'e6tВ9СdИД7g4УНЖzО1_ЪvЧЬjЙpАЭxwcsbkЮmnqfБurЫiПКlТР5hЯ3ЗyoШ2ЦЛЩМГ80ФХЕaЁ',
        'stepping': 'ИvЗ',
    },
    'Х': {
        'wiring': 'w6pmАruС1o7jЫqУЯЕЪzБЁЙКВМФc3sЦШЗyЛОb2gЬ9_nЩtГДЮkxlЭfХИНhad0Ж58ЧiП4РevТ',
        'stepping': 'КdХ',
    },
    'Ц': {
        'wiring': 'tЬЯШ9anyНk6i5ВpuОsze7b8Иmg0ЁЩvdГ_КЛРФЖХЭАЪoЗЫТxr4СhjМ3Пfcw2ДБЕЮЧlУЙ1Цq',
        'stepping': 'hcА',
    },
    'Ч': {
        'wiring': 'g_jhРИХkxbДПЕaЮuСmvЬ0ozМЁЯ5Л6ТidfБlЩФЫЭqeВrЖЗns7ШУ8pОw4cЦ3Кy2НГtЪЙ9А1Ч',
        'stepping': 'mЛl',
    },
    'Ш': {
        'wiring': 'АejgЮ96Л8ЯИtr5dЪЩuwД3bКРfpШlВ_Пv21izaoyМЧЙkЬЗ0ТqФЭБОНСУs7Ж4ЕhcЁЫxmХГnЦ',
        'stepping': 'm8Я',
    },
    'Щ': {
        'wiring': '8a9ЙЖdУЯВХbФ1М7jroghЪЛ26xЕcЮptИЩЭЧ_БeЬ4ОЦkР3sГvЗqШТПnДСuЁfКywm0АЫНzil5',
        'stepping': 'hpП',
    },
    'Ъ': {
        'wiring': 'ЫРТКfО2rХФoqjИ0b_i1ВwtН8Ц3ЩУГengЯdЭsСzkhЕ7Б6ЁЛalЗШЪЙПmy4pЧД9ЬЮЖАcvuМ5x',
        'stepping': 'wТЗ',
    },
    'Ы': {
        'wiring': 'lcn2wЧДСfjtТЙРХЖЩМЛЫmУЗ4yd_vqЭuГze036НaЪxКЯАri8Е71ЁБО9gbИhШВksФЦЮopЬ5П',
        'stepping': 'ЙcД',
    },
    'Ь': {
        'wiring': 'ХЭnТМyЕbrml8ЯГcВv1БpЖРЦСИ2h49ЫdНДЙШЛЬОkЗЩg_u3t6oЧФqЁfЮАКjz5Уax0П7iЪwse',
        'stepping': 'eЗn',
    },
    'Э': {
        'wiring': 'НoЬИqyw0ЗЪnЮxЙmvz7ЫlhШdОЖЛУbgk139ДЧtСaЕБЯjfu8МЁcАЭ6В24eКpФ_rsП5ЦРЩХiТГ',
        'stepping': 'fcО',
    },
    'Ю': {
        'wiring': 'ЗyeШЁ1ЩlХФЪhЦinБjpgВАДЯa0О_Н2КЖs8ЧbЕrТ6ЬxowМ9Йvq7ИЭЛ4dРtcЮСuУ3f5ЫПzГkm',
        'stepping': 'uЭ7',
    },
    'Я': {
        'wiring': 'nЮyЁЧМkw4pХД_uЯФqЫУdЕesvЬ9mzП1ЭtШЗИ7ЪfЖgТjГЩЦЛСВАoКН8ixhb60aРlОr2Б35Йc',
        'stepping': 'БЬ7',
    },
}

REFLECTORS = {
    'А': {
        'wiring': 'y0ЮД3В_СМА94Т61ЬЩЁ2wИБtПaУjvfШdОrЛ7u8ЯЖiЦЕxФhmzРЧНХГq5ЭpЫcКboselЪnЗЙkg',
        'plaintext': '1o',
    },
    'Б': {
        'wiring': '9tОЮfevЕЬКЁyФСrШМoЙbЗgЯ3lРБАЖЭПhkВuЪsj1qЩcДzn2Цm_У5pНИ8iГdw4ЛТx0Ч76ЫaХ',
        'plaintext': 'Фm',
    },
    'В': {
        'wiring': 'qОxnСН2ЮКАГ87dЕ6a5ЭzЫМЪcЯtjЩИkЖo9ДУВЬiПvfbЛ0eЦЗШ4Т_ФБwuЙshyР3g1ХrpmlЁЧ',
        'plaintext': 'Юh',
    },
    'Г': {
        'wiring': 'ndjbО8qШЮc3pxa2lgСВЪ_7ЁmПЛГЭsА9ИwФ4ЕХЬzТРeyНrМ5ЖЙ16hЫtЩКБi0ЯЦokЗУЧvfДu',
        'plaintext': 'rС',
    },
    'Д': {
        'wiring': 'Г0yЗ2Ж4ОФ_Л8ШЙИ1svqДЧrВПc96ЩwatЭЬfdon5k7РhxНЯЮЦi3УumБЫЪЁЕТСbpeХgКАМlzj',
        'plaintext': 'Иo',
    },
    'Е': {
        'wiring': 'КЖЮx0ЫoЛ3АЦЯЬpgn8ОЙ4ШyЭdv_j1ЪИ9МЩbПГsahЕ2rЗЧФ7ХСУkРuЁВfmwcleБНit65ТqДz',
        'plaintext': '0e',
    },
    'Ё': {
        'wiring': 'Оw7ХЛxsljiЮhЙЖЬТСФg_УЁbfГЧШРИy4ПvnЩВm0e5ЫaЕБqpurdЭzАЗ6НoЦk1КЯ89ДМЪc23t',
        'plaintext': 'xf',
    },
    'Ж': {
        'wiring': 'fЬЭrРaЙ8Ц_7ВБТШ9Лd23ЕЫНЩЗСОmlЧКu1ЪyУgДqПwАМeznИ45iГoxЖvbcЯЮ6ЁstФХ0khpj',
        'plaintext': 'ИУ',
    },
    'З': {
        'wiring': 'Зx2k0НФОysdЦ19СБЧГj74ВПbi3УpvrХМЩЭaЪЛ_ЙЕfhw5o6АgДlq8ЁИЮЯЖЫЬemczuРТtШnК',
        'plaintext': 'lЦ',
    },
    'И': {
        'wiring': 'jqmfzd8ИЬaХЮcКxОb4y5ЁЧЛose91723ЭuЦСhРnwПЩpМЙЗЯЪШkЖvФНУ0iЕlТЫБГДrt_ВgА6',
        'plaintext': 'ЯТ',
    },
    'Й': {
        'wiring': 'gЧЕlЖЛaЯm90di5_1ЫКu3sРШДЭЁ6ГЩБxczeТ7УrfЦФ2ЬvЪЗЙНЮМbwВСqПyХhkpОt8nАИ4jo',
        'plaintext': 'Дx',
    },
    'К': {
        'wiring': 'oЬЙedНvslЮВipxamЪ0hЗПgБn_2ЦwkХЁТДИtЖcЧЭ6fШu5ФЕ4СГАКОЯq9bЛjЩr3z1УРМ87Ыy',
        'plaintext': '5Р',
    },
    'Л': {
        'wiring': 'claОtЩ7ЬЙУmbkЫ5Р6ЗveЖsyИwz4Ъ3ФСНТurxi8ЦЯЕd_pДЁjГ9Л21fБnhЮЭМ0ШЧВАoqgКХП',
        'plaintext': '3В',
    },
    'М': {
        'wiring': 'МОcp4АktЩ5gЯЖwШdКuvhrsnПЮЁfЭУНЗЕzmДТ7qЦaГbx_ЫИВЬЧЛХoi0СФБylЪ321ej9Й86Р',
        'plaintext': '69',
    },
    'Н': {
        'wiring': 'mПФ5goeХШ9u8a2f4yЗЛvktОЫqДЙГ0БzНИ7rЁАМsКЕwbЧЭЦ6chТРiЯ_x1С3ЩВЬnЮpdУЖljЪ',
        'plaintext': 'Ыx',
    },
    'О': {
        'wiring': 'ЪИz4rh_fП5РКpС0mВeБЛЯЩФ2ЙcДsqЗАЖ6ЕГbylt71ЮiknЭЫw9ЧЦ8vaУ3ТОuoНxЬdjЁМШХg',
        'plaintext': 'lК',
    },
    'П': {
        'wiring': 'baЫЧ_46ЦУnА59jЮЩДЖФВЬЕХ2Э1kЙtЪqvШrРЯБТ83ОНСЗПКiswhdЁpГcuyoИ7zxМflg0Лme',
        'plaintext': 'pЩ',
    },
    'Р': {
        'wiring': 'rСШ3АЙhgnДЬПУi_sГapxХТОtБЫeyРqjЧЮЯ98fЩ62ЦwlВbvmЪuНЕcКФzk1ЁЖ4ЭМd07Л5ИЗo',
        'plaintext': 'ra',
    },
    'С': {
        'wiring': 'jПoА_УС3ШaЛЯЁ5cЫtЭФqРЧyДwНdЕ28xБmЩХТЬ6kЦz0bugИfsЗМviЖ1pЙr4lОЪВhЮnК9Г7e',
        'plaintext': 'kЛ',
    },
    'Т': {
        'wiring': 'Ъ9Ф4Мz_xЁuБrАР3sГlpУjИШhВfmkyqЕДi81v7ЮТeХС5nОЛtcНЩЭwЦa6ЯЧКЬ2З0odПЫЙЖbg',
        'plaintext': 'g_',
    },
    'У': {
        'wiring': '19НЪwЛФsyЙЦ7ЮЕБЧЁЖhУР3eСiЫГo5А_nqr0ШjОfХcК4uxЩtgМkpИТdz82m6ЗaЭvПВЯlЬbД',
        'plaintext': 'pЧ',
    },
    'Ф': {
        'wiring': 'iЁmhvundaЙУГcgt5ЫОЗofe3ДМЛЪЩ2lxХbПs0jЬzyЦrЖЧ7ФkТЕНР1БАqК8_9ИШВw6p4СЭЯЮ',
        'plaintext': 'Зs',
    },
    'Х': {
        'wiring': 'ЁnЮС6ЫЖ50sЬp4b1lutjrqХШЧzyИЭЩ9МПagКАЪЗРДЦЯЕЛd_28vНxwВЙfkБcОioУ7mhe3ФГТ',
        'plaintext': 'fЫ',
    },
    'Ц': {
        'wiring': 'С4t5Л1ЗО0yШ7АГpoДИzc3НЕЧjsmКЁnqwВ9gr2БeЦvhХТaР6ЮПМxkЯЬ_Ъ8ФЩifЙubdУlЭЖЫ',
        'plaintext': 'b4',
    },
    'Ч': {
        'wiring': '7cbВЖjСЯmfvПi1ЁЪ4ЕЗБРkДЩИАztdЦwroesy6ХМЛТ5lugНФУКГ8_xp3ЭЬ2h9nЮЫqОЙaЧ0Ш',
        'plaintext': 'ЭЬ',
    },
    'Ш': {
        'wiring': 'БqpАГЪ2kЮВhxНzСcbЯЛ53ЧШlДndajeyЙ_1ПЭЕЦsУm7ЗЩo0М68КvwРf49ИirТЖguЫtФОХЬЁ',
        'plaintext': 'eГ',
    },
    'Щ': {
        'wiring': 'ИЯ4tqiД9fkj2Й5Ю7e6ФdГ_СЕЁВЫ3zugxyХТamЛКЭЦЧЬЩwЗ8sЖНО0Р1АПМobШЪlБcnrpУhv',
        'plaintext': '2l',
    },
    'Ъ': {
        'wiring': 'ogn2Рhbf1ЭЮ4Нca3xФtsДЪЕq_ЩЁЙШЦuwАХЫ7БОЯ9mК0e5Ч8rЖГТВzvЗ6jkЛПidplСЬИУМy',
        'plaintext': 'Эj',
    },
    'Ы': {
        'wiring': '0НШqsВ4m2t5whЗЕ7dvej3rlБКЪ1xf8_oЯЭnЧФyЩТbР6О9МЫЙЦХИcЛzУЮЖЬЁaАiugkПpГСД',
        'plaintext': 'ЙФ',
    },
    'Ь': {
        'wiring': 'ЭЬtШАhlfГН9gДУСЕ6ИЪc4ЁБЦ0Яew_impvЫХrР15ЮjЩ2Йo3n8Зx7dОsЖbaМzyКПТuЛqЧФkВ',
        'plaintext': 'aЭ',
    },
    'Э': {
        'wiring': 'КЩБ1ЁЬФjwh9r4ЕПЮУlНРХЙiyxЦИc8ЯШneТЛАvaЗ7sЫotЧЖqguzСДb5Оf3pГ6d_ЭmЪ0МВk2',
        'plaintext': 'uХ',
    },
    'Ю': {
        'wiring': 'ИzД4ЫЗm5l6ЁigЭ7wВНЪС_Тp2ОbПЧqЮc3kЛfa9ЦЖ8ryАЬtv1Ш0КБФЯseРnГЩХУxЕdhjoМЙu',
        'plaintext': 'fЗ',
    },
    'Я': {
        'wiring': 'n9ЮВЫ2ЛpsЕ0ЭЬaСhХЩiШФА67zyvПd83jЖЁЙОЗЦgУ1ИБ_oЯМuqК5tr4emlcТkНfДЪЧwxГbР',
        'plaintext': 'qХ',
    },

}
