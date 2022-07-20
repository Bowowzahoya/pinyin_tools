# pinyin_tools

Tools for dealing with pinyin strings.

## Splitting pinyin strings
### split()
A function to split a string in pinyin syllables. As there can be multiple possibilities, the function returns a set of the possibilities.

```
split_possibilities = split_word("liange")
```

This will return possibilities like:
- Li, an, ge
- Lian, ge
- Liang, e

This function, like all other functions except lazify() have a "mode" keyword. 
- mode="lazy" assumes lazy pinyin (pinyin with no tones)
- mode="extended" assumes lazy pinyin with alternative writings, such as lv or lyu.
- mode="tones" assumes pinyin with tones
- mode="tones_extended" assumes pinyin with tones and alternative writings.

## Converting Pinyin strings
### lazify()
Convert a string with tones to lazy pinyin (pinyin without tones).

```
string = split_word("nǐ hǎo")
```
Returns "ni hao".

## Identifying Pinyin strings
### is_pinyin()
Check if a string could be pinyin ("pier" returns True, "peer" returns False).

```
if is_pinyin("ni hao"):
    print("This is a pinyin string!")
```

## Chinese names
### is_name()
Check if a pinyin string could be a Chinese pinyin name.

```
if is_pinyin("ouyang lili"):
    print("This is a pinyin name!")

if not is_pinyin("ouhang lili"):
    print("This is not a pinyin name!")
```

### is_first_name()
Same for first name.

### is_last_name()
Same for last name.
