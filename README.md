# Spark

Spark is a font for creating sparklines in text. It uses OpenType's contextual alternates and requires no Javascript. At the moment it is compatible with Microsoft Word (2011 and later), Adobe Creative Cloud applications, Chrome 33+, Safari 6+, Internet Explorer 10+.

Spark uses the `calt` feature of OpenType to perform simple replacement operations on numbers. It takes strings like 123{30,60,90}456 and output a sparkline with three datapoints (30, 60, and 90) – the numbers outside of the brackets are not transformed.

It works like this:

```
ignore sub zero' comma space;
sub braceleft' zero' braceright' by chart.000;
sub braceleft' zero' comma' by chart.000;
sub zero' comma' by chart.000;
sub zero' braceright' by chart.000;
```

The method is a bit brute-force in nature. There is very possibly a better way to do this.

Because the replacements are all hard coded, each file can only take input of 0–100[^1] and the scale is always 0–100. There is no logic and Spark is relatively dumb as technology goes.

[^1]: The dotline version only goes from 0–9 because it isn't just replacing a single unit, but reading the next number on to determine what line to draw from any given point. There is no theoretic reason why this could not be extended to 100, or 1000, or beyond. However at the current moment we don't know how to script the generation of the many glyphs needed to do this so they all need to be drawn by hand.

See also: http://stateofwebtype.com/
