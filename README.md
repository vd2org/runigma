# periodic

RuNigma is a fictional cypher machine inspired by World War 2's Enigma Machines.

# Setup

```bash
pip install runigma
```


# Example usage

```python
from runigma import RuNigmaMachine

rotors = 'Ё Ь Д Н Й'
reflector = 'Ш'
ring_settings = 'a _ y g Б'
plugboard_settings = 'xЕ hЬ КМ Тn iЗ АЛ ЮЫ Бt z8 ОШ wЯ y0 a7 4Ъ СЖ p6 Эe g_ 2b dc'

machine = RuNigmaMachine.from_key_sheet(rotors=rotors, reflector=reflector,
                                        ring_settings=ring_settings,
                                        plugboard_settings=plugboard_settings)

machine.set_display('ЯХ3ОЪ')

crypted = machine.process_text('hello world')

print(crypted)
# displays: БЮУЦwЛgcЭЕМ
```

# Command line tools

## runigma

This tool can be used for encipher and decipher text.

```bash
runigma --key-file=enigma.keys -s ФСИАР -t HELLOXWORLDX
```

```bash
runigma -r A Б В Г Д -i a b c d -p AB CD EF GH IJ KL MN -u Ф -s АУГСД
```

## runigma-sheet

This tool can be used for generate new key sheet file.

```bash
runigma-sheet > keysheet.txt
```
