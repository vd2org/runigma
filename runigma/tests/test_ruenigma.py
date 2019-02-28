# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of Py-Enigma, the Enigma Machine simulation.
# Py-Enigma is released under the MIT License (see License.txt).

"""Tests for the EnigmaMachine class."""

import unittest

from ..machine import RuNigmaMachine


class Vector1TestCase(unittest.TestCase):
    """This test test-vector 3 for RuNigma cypher"""

    IN = 'abcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789_'
    OUT = 'Нh5sh8ДТegkМd34zТНutdКpЛtЬ71БТmbjЕМПiФkl0abРФmЫvpХАЩwi0ЮУАhРz6tЛЬАЮ4nИ'

    def setUp(self):
        self.machine = RuNigmaMachine.from_key_sheet(rotors='А А А А А',
                                                     reflector='А',
                                                     ring_settings='a a a a a',
                                                     plugboard_settings='')
        self.machine.set_display('aaaaa')

    def test_simple_encrypt(self):
        cipher_text = self.machine.process_text(self.IN)
        self.assertEqual(cipher_text, self.OUT)

    def test_simple_decrypt(self):
        plain_text = self.machine.process_text(self.OUT)
        self.assertEqual(plain_text, self.IN)


class Vector2TestCase(unittest.TestCase):
    """This test test-vector 2 for RuNigma cypher"""

    IN = "ЖИЛИ_В_КВАРТИРЕ_СОРОК_ЧЕТЫРЕ_СОРОК_ЧЕТЫРЕ_ВЕСЕЛЫХ_ЧИЖА_ЧИЖ_СУДОМОЙКА_ЧИЖ_ПОЛОМОЙКА_ЧИЖ_ОГОРОДНИК_ЧИЖ_ВОДОВ" \
         "ОЗ_ЧИЖ_ЗА_КУХАРКУ_ЧИЖ_НА_ПОСЫЛКАХ_ЧИЖ_ЗА_ХОЗЯЙКУ_ЧИЖ_ТРУБОЧИСТ_ПЕЧКУ_ТОПИЛИ_КАШУ_ВАРИЛИ_СОРОК_ЧЕТЫРЕ_ВЕСЕЛ" \
         "ЫХ_ЧИЖА_ЧИЖ_С_ПОВАРЕШКОЙ_ЧИЖ_С_КОЧЕРЕЖКОЙ_ЧИЖ_С_КОРОМЫСЛОМ_ЧИЖ_С_РЕШЕТОМ_ЧИЖ_НАКРЫВАЕТ_ЧИЖ_СОЗЫВАЕТ_ЧИЖ_РА" \
         "ЗЛИВАЕТ_ЧИЖ_РАЗДАЕТ_КОНЧИВ_РАБОТУ_БРАЛИСЬ_ЗА_НОТЫ_СОРОК_ЧЕТЫРЕ_ВЕСЕЛЫХ_ЧИЖА_ДРУЖНО_ИГРАЛИ_ЧИЖ_НА_РОЯЛЕ_ЧИЖ" \
         "_НА_ЦИМБАЛЕ_ЧИЖ_НА_ТРУБЕ_ЧИЖ_НА_ТРОМБОНЕ_ЧИЖ_НА_ГАРМОНИ_ЧИЖ_НА_ГРЕБЕНКЕ_ЧИЖ_НА_ГУБЕ_СПАТЬ_ЗАХОТЕЛИ_СТЕЛЮТ_" \
         "ПОСТЕЛИ_СОРОК_ЧЕТЫРЕ_ВЕСЕЛЫХ_ЧИЖА_ЧИЖ_НА_КРОВАТИ_ЧИЖ_НА_ДИВАНЕ_ЧИЖ_НА_КОРЗИНЕ_ЧИЖ_НА_СКАМЬЕ_ЧИЖ_НА_КОРОБКЕ" \
         "_ЧИЖ_НА_КАТУШКЕ_ЧИЖ_НА_БУМАЖКЕ_ЧИЖ_НА_ПОЛУ_ЧИЖ_ТРИТИТИТИ_ЧИЖ_ТИРЛИТИРЛИ_ЧИЖ_ДИЛИДИЛИ_ЧИЖ_ТИТИТИ_ЧИЖ_ТИКИТИ" \
         "КИ_ЧИЖ_ТИКИРИКИ_ЧИЖ_ТЮТИЛЮТИ_ЧИЖ_ТЮТЮТЮ"
    OUT = "Ё5rji8КbЬ75ЯЩГЁТЯ_5pЦФxЬ6МuКuЭШЬtЪ1roВ6ЕЬ6fЩДsЮЫЖ_ЖЦoiХqЭ4ТЭ15УМx5ТШhДШuqЫzМjМ_ЮqcДs_ЖjФv18О5ФЕcvЩskweУПЫД" \
          "cЁ77h8ТК3sЧУШЕ2ФТk3eПtМЮqП6СhoКfezНЦЗЗ5weИt8oЩxnЫlАvЮЪv5rdЬqЭ4kЧЧ3Фz66xrФsЙ5Сl9iЧ3НЩПcК0tСfiЧМfxСЪХtЭ8ЧdcЯ" \
          "Рl22ДМЗШГАz76КРФyaГvЬБЪ5mЩМa385fcПtgЩjДБТh6_ВСБШЬu5bУ5Ц8kcЯqkЪoХekДШООНv3Ю85naЦe45Рn9nШqЖБ_gИdizЕПЛrЛnnМПy" \
          "ГЕЯiОА4ШДМБППcЗЫОН2m0uxЛЗs3Ь5fОvЖehmn8Б31ЫcoГНАcМ7yШИ8В3ЁhЮЬРЖeЧjПГШ9o68ЛЫНbiЪУЖЩЮРЩППМ0Й_ЯcМ_0fШ81u6uuЙ04" \
          "6МБИБЫkopБАШ5ДxЮРlЗhgf8ЧТНЧ9УfЯ4ЪИРneЙЬЁЪБyЦ1Чh7lfЖmpН1ЮФЩО5Пd76Н1ЧИМ4eЁfrКqjАФ0kПМf9ЁwzНroНxЪq8_5on7hДmtЖ" \
          "mbЯП3khЩfПyiФД14ЮЕzЯhТmСЪЧВБЕrnЕЖf8КЭfФgЬЬe7fВНei_qrЬДЮАШБpЬФЭЧП9pЦЦax74СbЛЧ68vdШbЙЧ6yЗПhОЬУho1ЫТttЕzЁ3ЪvЪ" \
          "3q5Ф2lПБ8vhoЪЙrАig_Ё9oВ8jБe3fЭИТ8Щrqtw1nОЖyНxТЕy2ЮЫqНИloК2Мzc08ВЬВЭa5l6zО9ЪvdayЙГЛ5qСxИЖКst0rЭЮxБtЙСvc92ЖИ" \
          "dДhЧЁwЩ5ВТs3pjdОxКЬД13ГiЧХc56b4УyЪЛ8ФНc"

    def setUp(self):
        settings = dict(rotors='Ь Ч Ю Г Ъ',
                        reflector='Ш',
                        ring_settings='r _ s Ч n',
                        plugboard_settings='zy Ю0 ЪЭ 6Ф ЯЫ ЙА wt lk ДР 3К q1 gm 9Ж uЧ ТЛ _2 ЩЕ ИМ hx fi')
        self.machine = RuNigmaMachine.from_key_sheet(**settings)
        self.machine.set_display('vhЯkК')

    def test_simple_encrypt(self):
        cipher_text = self.machine.process_text(self.IN)
        self.assertEqual(cipher_text, self.OUT)

    def test_simple_decrypt(self):
        plain_text = self.machine.process_text(self.OUT)
        self.assertEqual(plain_text, self.IN)


class Vector3TestCase(unittest.TestCase):
    """This test test-vector 3 for RuNigma cypher"""

    IN = "lorem_ipsum_dolor_sit_amet_consectetur_adipiscing_elit_sed_do_eiusmod_tempor_incididunt_ut_labore_et_dolor" \
         "e_magna_aliqua_ut_enim_ad_minim_veniam_quis_nostrud_exercitation_ullamco_laboris_nisi_ut_aliquip_ex_ea_com" \
         "modo_consequat_duis_aute_irure_dolor_in_reprehenderit_in_voluptate_velit_esse_cillum_dolore_eu_fugiat_null" \
         "a_pariatur_excepteur_sint_occaecat_cupidatat_non_proident_sunt_in_culpa_qui_officia_deserunt_mollit_anim_i" \
         "d_est_laborum"
    OUT = "Уh5nШУb1dЩМО__СqФdСГГg2ЬЧkЫПo3КВФtНВНН9Чf_qgЁМvЪЮКgАЙТБgЩЁm1hiuОp6o2ЕХЪbncЭrЗЫЪwШПiНСЦnh4bblxИЬЧЗ2Щ9СЦvnab" \
          "tИeЧ6ПЗХuСРxАiaУИЕЩБ6nqm9aresm7ФiО1ВЧjСlsЯА13ХНЛЛДhХaУi13ipeРuЫПЦ9s9ОЯ3lp2wНq3iЁpТgz5ЩКАut88ЛhЮСБgГ1ЮНЦ6gЗ" \
          "Мll8ЕlЪТМkeГ2qpФЕupЧШЖ4ubЁЗШАcЁЩ0Ш_ywЮЙrЬ0У3s_Ч9ЕjФiЖeУЮxФС1ЬЛЧМ0pbИЯhМЬwЬННaМП4makЗЛЁ3МВОТiyЁmvaЕМzАhК8Юg" \
          "cХdЭcixО0sДШОdt9ЙСmЙ_liЁxx9zzЯК4vЫМc9Ё6ЕpkТНЬНЖxЖhИДЧqКvgzte2zВЖwfЦЭНЖЫИА2ЛТЗЖЮr0g8Э7РwЩwzЖw4ЭСЦfiФЧjБu6ЖЖ" \
          "iЩkЙШnРmmЯ3uЭ"

    def setUp(self):
        settings = dict(rotors='О Н З Ё Д',
                        reflector='Э',
                        ring_settings='2 Ф u Щ n',
                        plugboard_settings='ЭЧ ЖЪ А2 ЁВ tЮ j5 k8 rb Оv en yЫ pТ 1З Бl 9Й Хc Пh gЬ da iЩ')
        self.machine = RuNigmaMachine.from_key_sheet(**settings)
        self.machine.set_display('Э03Нj')

    def test_simple_encrypt(self):
        cipher_text = self.machine.process_text(self.IN)
        self.assertEqual(cipher_text, self.OUT)

    def test_simple_decrypt(self):
        plain_text = self.machine.process_text(self.OUT)
        self.assertEqual(plain_text, self.IN)
