# Tutorial: using the AtF Spark font for creating sparklines in text

*This tutorial is taken and amended from [a version on the Online Journalism Blog](https://onlinejournalismblog.com/2017/09/21/how-to-use-the-atf-spark-font-for-creating-charts-with-only-text/#more-25179)*

AtF Spark is "a typeface for creating sparklines in text" created by After The Flood. The [GitHub repo](https://github.com/aftertheflood/spark) is useful, but assumes some prior knowledge. This tutorial is designed to explain how to use it if you're not already familiar with web fonts and other technicalities of web design.

## Breaking down the elements

To create a webpage with a Spark chart you need the following ingredients:

1. A HTML page. Specifically, we need to make sure that part of the HTML includes some numbers that the font can work with.
2. A CSS file (style sheet). The CSS file is what 'styles' part of the HTML into the Spark font.
3. One of the AtF Spark fonts. This needs to be downloaded from the Spark GitHub repo's ['Output/Webfonts' folder](https://github.com/aftertheflood/spark/tree/master/Output/Webfonts) and stored in the same place as the CSS file.
4. Links between all three: the HTML file needs to link to the CSS style sheet file, and the CSS style sheet needs to link to the font file.

## Creating the HTML page

Let's make the HTML page first. I've created mine using the text editor Atom, and saved it as 'index.html'.

What HTML you put in the page doesn't really matter - but you must have a section that is going to be turned into the chart, and a link to a stylesheet.

The chart section needs to include a series of numbers separated by commas, inside **curly brackets**, like so:

`<span class="barchart">4 {4,0,0,0,6,29,70} 7</span>`

Note that there should be **no spaces** after the commas, and all numbers must be between 0 and 100, otherwise it won't work. Any numbers outside the brackets will be styled as normal nummbers, so those can be used as a sort of legend, to describe the start and end points of the chart.

The example above also has a `<span>` tag with a `class` attribute. This means we can *target*, or rather *select*, the text inside with a style sheet, in the second step.

To do that, we need to make sure that there is a link to that style sheet. Here it is, inside the `<head>` tags:

`<link rel="stylesheet" href="css/style.css">`

But where is that stylesheet? We'll need to create it, in a minute.

The full HTML for a page including the numbers, and a link to the stylesheet we're about to create, is below:

```html
<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Spark font example</title>
      <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <p>There were 70 Airprox reports involving drones coming close to aircraft over the UK in 2016 - compared to 29 in 2015 and just 4 in 2010 <span class="barchart">4 {4,0,0,0,6,29,70} 70</span>. There have been 33 incidents up to May 2017. </p>
  <p>That chart above is created using the font Spark: each bar of the chart is actually a number.</p>
  <p>The font to turn it into a chart needs to be stored in the same place as the CSS file.</p>
</body>
</html>
```

## Creating the stylesheet

Next we need to create the stylesheet that we've just linked to. The link said `<link rel="stylesheet" href="css/style.css">` so this file needs to be called 'style.css', and it needs to be in the same place as your 'index.html' file, but inside a folder called 'css'. (You could put it elsewhere, and/or call it anything else, as long as you change the link accordingly)

### Bringing fonts into a stylesheet

To use this font in the webpage we need to add a line at the top of the CSS file:

```css
@font-face {
  font-family: spark;
  src: url(spark-bar-medium.woff);
}
```

The `@font-face` rule, as [one explainer puts it](https://css-tricks.com/snippets/css/using-font-face/): "allows custom fonts to be loaded on a webpage. Once added to a stylesheet, the rule instructs the browser to download the font from where it is hosted, then display it as specified in the CSS."

Anything in curly brackets after `@font-face` specifies the parameters of how that font is loaded. First, `font-family:` *names* the font for our stylesheet's purposes. This name can then be used elsewhere to refer to it. In this case we've named it `spark`.

Second, `src:` specifies where the font should be loaded from. In this case, it also uses `url()` and then inside those brackets, the location of the file. As it happens, this doesn't *look* like a URL - but if you imagine this webpage on the web, it simply means it's going to look for a file with that name in the same location (on the server) as the webpage.

Where is this file? We'll come on to that in a minute.

First, we need to add another rule which applies this font to the `span` created earlier. Here it is:

```css
span.barchart {
    font-family: spark;
  font-size: 24px;
  color: orange;
}
```

First, `span.barchart` targets, or selects, anything with the HTML tag `<span>` and the `class` attribute `="barchart"` (the period `.` here means 'class'). Remember that the number series we created earlier is in exactly such a tag.

Then we specify three rules about how anything selected in this way should be styled. The first is `font-family: spark;`. This is where that font - named 'spark' earlier - is applied.

The next two lines add a font size and colour, too, but these are not essential.

The full CSS file, then, looks like this (it includes some extra lines that aren't essential but [add a bit of browser-proofing](https://helpx.adobe.com/typekit/using/open-type-syntax.html#calt)):

```css
/* This needs to be hosted in the same place as the css file */
@font-face {
  font-family: spark;
  src: url(spark-bar-medium.woff);
  font-variant-ligatures: contextual;
  -moz-font-feature-settings: "calt";
  -webkit-font-feature-settings: "calt";
  font-feature-settings: "calt";
}

span.barchart {
    font-family: spark;
  font-size: 24px;
  color: orange;
}
```

## Finally, download the font file to the same place as the CSS file

The Spark font can be downloaded from the Spark GitHub repo's ['Output/Webfonts' folder](https://github.com/aftertheflood/spark/tree/master/Output/Webfonts). At the moment there are 6 folders in there: 3 bar chart options (medium, narrow and thin), 2 dot charts (medium and small), and 1 dot line (medium).

You can [see some examples of the different chart types in action on the Spark page on the After The Flood website](http://aftertheflood.co/projects/atf-spark).

Click on the folder for the chart/font you want to use (note that the line chart is limited to numbers between 0 and 9), and you should see 5 files in that folder. These are 5 different formats. We've used the '.woff' format, so click on that version, and you should be taken to a page which doesn't look like much (GitHub cannot show it in any way, so just shows a grey box instead). Click **Download** to download this file to your computer.

Once downloaded, move the file to the same folder as the CSS file.

Now that link in the CSS file should work. And the link in the HTML file pointing to the CSS file means that styles in that sheet should now be applied to the HTML. If you load or refresh the HTML page you should now see the effect.


## The quick version

The quickest way of achieving the results above is to:

1. Export [my Codepen pen on Spark](https://codepen.io/paulbradshaw/pen/zEBzmE) as a zip file (the button to export should be in the bottom right corner).
2. Unzip the export. You should now have a folder with an `index.html` file and a `css` folder containing a `style.css` file.
3. Download the [font file from the AtF Spark GitHub repo](https://github.com/aftertheflood/spark/blob/master/Output/Webfonts/Bar%20-%20medium/spark-bar-medium.woff). That link takes you to the 'spark bar medium' font, but you can also find fonts for other widths of bar chart and for line charts in [the 'Output/fonts' folder](https://github.com/aftertheflood/spark/tree/master/Output/Webfonts)
4. Put that file in the `css` folder
5. The chart should now be working based on the numbers in curly brackets on the HTML page. Just change those numbers to change the text - or copy and paste it (including the `<span>` ) to create new charts.

You can also find a webpage and stylesheets in the '/docs' folder of this repo, which generates a websites at [https://paulbradshaw.github.io/using-spark/](https://paulbradshaw.github.io/using-spark/)

*Note: At the moment it is "compatible with Microsoft Word (2011 and later), Adobe Creative Cloud applications, Chrome 33+, Safari 6+, Firefox 4+, and Internet Explorer 10+. (See: http://stateofwebtype.com/ for a fuller listing of browser compatibility.)"*
