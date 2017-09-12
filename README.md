# Spark

Spark is a typeface for creating sparklines in text. It uses OpenType's *contextual alternates* and requires no Javascript, though it does require a modern-ish browser that can make use of OpenType features in text. At the moment it is compatible with Microsoft Word (2011 and later), Adobe Creative Cloud applications, Chrome 33+, Safari 6+, Firefox 4+, and Internet Explorer 10+. (See: http://stateofwebtype.com/ for a fuller listing of browser compatibility.)

Spark uses the `calt` feature of OpenType to perform simple replacement operations on numbers. It takes strings like `123{30,60,90}456` and outputs a sparkline with three datapoints (30, 60, and 90) – the numbers outside of the brackets are not transformed.

When using the webfonts in a browser, you are supposed to explicitly enable the `calt`, however it seems that these days `calt` is enabled by default and you don't need to do anything to make it work other than assign the font to your text. Still, better safe than sorry. The CSS to explicitly turn on the feature looks like this (example pilfered from https://helpx.adobe.com/typekit/using/open-type-syntax.html#calt):

```
.class {
  font-variant-ligatures: contextual;
  -moz-font-feature-settings: "calt";
  -webkit-font-feature-settings: "calt";
  font-feature-settings: "calt";
}
```

Inside the font files the code that powers the replacement operation works like this:

```
ignore sub zero' comma space;
sub braceleft' zero' braceright' by chart.000;
sub braceleft' zero' comma' by chart.000;
sub zero' comma' by chart.000;
sub zero' braceright' by chart.000;
```

The method is a bit brute-force in nature. There is very possibly a better way to do this and the close reader will note that there are ways to break the operation described above. For this reason you need to enter the text for the sparkline in a fairly precise format (e.g., don't put spaces after the comma or the glyph replacement doesn't happen).

Because the replacements are all hard coded, each file has a fixed scale of input it can take. The dot and bar versions go from 0–100. The dot-line version only goes from 0–9 because it isn't just replacing a single unit, but reading the next number on to determine what line to draw from any given point. There is no theoretical reason why this could not be extended to 100, or 1000, or beyond. However, while we can script the creation of the rules, at the current moment we don't know how to script the generation of the many, many glyphs needed to do this, so they all need to be (sort of) drawn by hand. This is made extra difficult because each angle of line needs to be optically adjusted so it *looks* like it is the same thickness as all the others – for a vertical and horizontal line to appear to be the same thickness the vertical line need to be thicker than horizontal line because your eyeballs are aligned horizontally, not vertically. Optics!

Spark is relatively dumb as technology goes, but it works. See it working on our [website](http://aftertheflood.co/projects/atf-spark).

### About us
[After the flood](http://aftertheflood.co/) is a design company based in London. We make new digital products and we believe data is the building material of the modern, 21st-century business. Using lean concepts, we collaborate with internal teams to harness their data and create products that users love. Organisations such as the NHS, Google, Nikkei and UEFA choose us to complement their domain knowledge with our experience in data products across many sectors, from equity finance to sports entertainment.

### License
Spark is free to use and modify. We'd love for you to contribute or fork the project.
