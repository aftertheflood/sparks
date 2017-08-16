# Spark

Spark is a font for creating sparklines in text. It uses OpenType's contextual alternates and requires no Javascript. At the moment it is compatible with Microsoft Word (2011 and later), Adobe Creative Cloud applications, Chrome 33+, Safari 6+, Internet Explorer 10+.

Spark uses the calt feature of OpenType to perform simple replacement operations on numbers. It works like this:

```
ignore sub zero' comma space;
sub braceleft' zero' braceright' by chart.000;
sub braceleft' zero' comma' by chart.000;
sub zero' comma' by chart.000;
sub zero' braceright' by chart.000;
```

See also: [http://stateofwebtype.com/]
