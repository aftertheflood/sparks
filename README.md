# Spark

Spark is a typeface for creating sparklines in text. It uses OpenType's *contextual alternates* and requires no Javascript, though it does require a modern-ish browser that can make use of OpenType features in text. At the moment it is compatible with Microsoft Word (2011 and later), Adobe Creative Cloud applications, Chrome 33+, Safari 6+, Firefox 4+, and Internet Explorer 10+. (See: http://stateofwebtype.com/ for a fuller listing of browser compatibility.)

Spark uses the `calt` feature of OpenType to perform simple replacement operations on numbers. It takes strings like `123{30,60,90}456` and outputs a sparkline with three datapoints (30, 60, and 90) – the numbers outside of the brackets are not transformed.

The code that powers the replacement operation works like this:

```
ignore sub zero' comma space;
sub braceleft' zero' braceright' by chart.000;
sub braceleft' zero' comma' by chart.000;
sub zero' comma' by chart.000;
sub zero' braceright' by chart.000;
```

The method is a bit brute-force in nature. There is very possibly a better way to do this and the close reader will note that there are ways to break the operation described above. For this reason you need to enter the text for the sparkline in a fairly precise format (e.g., don't put spaces after the comma).

Because the replacements are all hard coded, each file has a fixed scale of input it can take. The dot and bar versions go from 0–100. The dot-line version only goes from 0–9 because it isn't just replacing a single unit, but reading the next number on to determine what line to draw from any given point. There is no theoretic reason why this could not be extended to 100, or 1000, or beyond. However, while we can script the creation of the rules, at the current moment we don't know how to script the generation of the many, many glyphs needed to do this, so they all need to be drawn by hand.

Spark is relatively dumb as technology goes, but it works.


### License
Spark is free to use and modify. We'd love for you to contribute or fork the project.
