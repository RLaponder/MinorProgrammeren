/****************************************************************************
 * README.md
 *
 * Computer Science 50
 * Robin Laponder
 *
 * Questions for 'whodunit'.
 ***************************************************************************/

## What's `stdint.h`?

Een headerfile die specificeert hoe groot bepaalde types integers zijn.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Dit zijn unsigned en signed integer types. Deze worden gebruikt zodat je niet hoeft te detecteren hoe groot een bepaalde int is.
Daarnaast worden ze hetzelfde gebruikt op verschillende platformen.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

1, 4, 4, 2

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

42 4d

## What's the difference between `bfSize` and `biSize`?

bfSize is het formaat van het hele .bmp bestand en dus variabel, biSize is het formaat van BITMAPINFORHEADER (40 bytes).

## What does it mean if `biHeight` is negative?

Dan is de afbeelding top-down, wat wil zeggen dat de bovenste rij in de afbeelding ook de eerste rij bytes in het geheugen is.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

Als het bestand niet gevonden kan worden.

## Why is the third argument to `fread` always `1` in our code?

Het bestand wordt pixel voor pixel gelezen.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

Het verplaatst naar een specifiek punt in het bestand, in dit geval skipt het over de padding.

## What is `SEEK_CUR`?

Geeft de huidige positie van de file pointer aan.
