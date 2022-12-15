---
title: Binary Math + Operations
layout: default
description: A Binary Math illustrative application using HTML, Liquid, and JavaScript.
permalink: /frontend/binary
image: /images/binary.png
tags: [html, liquid, javascript]
week: 13
type: pbl
---

<!-- Hack 1: add a character display to text when 8 bits, determine if printable or not printable -->
<!-- Hack 2: change to 24 bits and add a color code and display color when 24 bits, think about display on this one -->
<!-- Hack 3: do your own thing -->

{% assign BITS = 3 %}


<div class="container bg-primary">
    <header class="pb-3 mb-4 border-bottom border-primary text-dark">
        <span class="fs-4">Binary Math with Conversions</span>
    </header>
    <div class="row justify-content-md-center">
        <div class="col-8">
            <table class="table">
            <tr id="table">
                <th>Plus</th>
                <th>Binary</th>
                <th>Octal</th>
                <th>Hexadecimal</th>
                <th>Decimal</th>
                <th>Minus</th>
            </tr>
            <tr>
                <td><button type="button" id="add1" onclick="add(1)">+1</button></td>
                <td id="binary">00000000</td>
                <td id="octal">0</td>
                <td id="hexadecimal">0</td>
                <td id="decimal">0</td>
                <td><button type="button" id="sub1" onclick="add(-1)">-1</button></td>
            </tr>
            </table>
        </div>
        <div class="col-12">
            {% comment %}Liquid for loop includes last number, thus the Minus{% endcomment %}
            {% assign bits = BITS | minus: 1 %} 
            <table class="table">
            <tr>
                {% comment %}Build many bits{% endcomment %}
                {% for i in (0..bits) %}
                <td><img class="img-responsive py-3" id="bulb{{ i }}" src="{{site.baseurl}}/images/bulb_off.png" alt="" width="40" height="Auto">
                    <button type="button" id="butt{{ i }}" onclick="javascript:toggleBit({{ i }})">Turn on</button>
                </td>
                {% endfor %}
            </tr>
            <tr>
                {% comment %}Value of bit{% endcomment %}
                {% for i in (0..bits) %}
                <td><input type='text' id="digit{{ i }}" Value="0" size="1" readonly></td>
                {% endfor %}
            </tr>
            </table>
        </div>
    </div>
</div>

<script>
    const BITS = {{ BITS }};
    const MAX = 2 ** BITS - 1;
    const MSG_ON = "Turn on";
    const IMAGE_ON = "{{site.baseurl}}/images/bulb_on.gif";
    const MSG_OFF = "Turn off";
    const IMAGE_OFF = "{{site.baseurl}}/images/bulb_off.png"

    // Above are assignents or functions that are procedural abstractions
   
   // return string with current value of each bit
    function getBits() {
        let bits = "";
        for(let i = 0; i < BITS; i++) {
        bits = bits + document.getElementById('digit' + i).value;
        }
        return bits;
    }
    // setter for DOM values
    function setConversions(binary) {
        document.getElementById('binary').innerHTML = binary;
        // Octal conversion
        document.getElementById('octal').innerHTML = parseInt(binary, 2).toString(8);
        // Hexadecimal conversion
        document.getElementById('hexadecimal').innerHTML = parseInt(binary, 2).toString(16);
        // Decimal conversion
        document.getElementById('decimal').innerHTML = parseInt(binary, 2).toString();
    }
    //
    function decimal_2_base(decimal, base) {
        let conversion = "";
        // loop to convert to base
        do {
        let digit = decimal % base;
        conversion = "" + digit + conversion; // what does this do?
        decimal = ~~(decimal / base);         // what does this do?
        } while (decimal > 0);                  // why while at the end? what is ~~?
        // loop to pad with zeros
        if (base === 2) {                        // only pad for binary conversions
        for (let i = 0; conversion.length < BITS; i++) {
            conversion = "0" + conversion;
        }
        }
        return conversion;
    }

    // toggle selected bit and recalculate
    function toggleBit(i) {
        //alert("Digit action: " + i );
        const dig = document.getElementById('digit' + i);
        const image = document.getElementById('bulb' + i);
        const butt = document.getElementById('butt' + i);
        // Change digit and visual
        if (image.src.match(IMAGE_ON)) {
        dig.value = 0;
        image.src = IMAGE_OFF;
        butt.innerHTML = MSG_ON;
        } else {
        dig.value = 1;
        image.src = IMAGE_ON;
        butt.innerHTML = MSG_OFF;
        }
        // Binary numbers
        const binary = getBits();
        setConversions(binary);
    }
    // add is positive integer, subtract is negative integer
    function add(n) {
        let binary = getBits();
        // convert to decimal and do math
        let decimal = parseInt(binary, 2);
        if (n > 0) {  // PLUS
        decimal = MAX === decimal ? 0 : decimal += n; // OVERFLOW or PLUS
        } else  {     // MINUS
        decimal = 0 === decimal ? MAX : decimal += n; // OVERFLOW or MINUS
        }
        // convert the result back to binary
        binary = decimal_2_base(decimal, 2);
        // update conversions
        setConversions(binary);
        // update bits
        for (let i = 0; i < binary.length; i++) {
        let digit = binary.substr(i, 1);
        document.getElementById('digit' + i).value = digit;
        if (digit === "1") {
            document.getElementById('bulb' + i).src = IMAGE_ON;
            document.getElementById('butt' + i).innerHTML = MSG_OFF;
        } else {
            document.getElementById('bulb' + i).src = IMAGE_OFF;
            document.getElementById('butt' + i).innerHTML = MSG_ON;
        }
        }
    }
</script>

<style type="text/css">
	.jumbotron{
	width : 60%;
	margin : auto;
	text-align: center;
	}

	#output{
	border: 2px solid black;
	min-height: 60px;
	text-align: right;
	font-weight: bold;
	font-size: 20px;
	}

	.btn{
	min-width: 120px;
	border: 2px solid black;
	}
</style>

<script type="text/javascript">
    var scr = ""; //declared as global v
    function calculate() {
        if (scr.indexOf("+") != -1) {
            // If + is present in the string
            // String obtained from scr is split
            var num = scr.split("+"); 
              
            // The splitted string stores in num array
            var x = parseInt(num[0], 2); 
            
            // The num[0] and num[1] are the two binary 
            // numbers resp
            var y = parseInt(num[1], 2); 
            var sum = x + y;
            var ans = sum.toString(2);
        } else if (scr.indexOf("-") != -1) {
            
            // If - is present in the string
            var num = scr.split("-");
            var x = parseInt(num[0], 2);
            var y = parseInt(num[1], 2);
            var sub = x - y;
            var ans = sub.toString(2);
        } else if (scr.indexOf("*") != -1) {
             
            // If * is present in the string
            var num = scr.split("*");
            var x = parseInt(num[0], 2);
            var y = parseInt(num[1], 2);
            var mul = x * y;
            var ans = mul.toString(2);
        } else if (scr.indexOf("/") != -1) {
            
            // If / is present in the string
            var num = scr.split("/");
            var x = parseInt(num[0], 2);
            var y = parseInt(num[1], 2);
            var div = x / y;
            var ans = div.toString(2);
        }
        scr = ans;
        document.getElementById("output").innerHTML = scr;
  
    function input(ch) {
        scr += ch;
        document.getElementById("output").innerHTML = scr;
  
    function backspace() {
        var b = document.getElementById("output").innerHTML;
        scr = b.substring(0, b.length - 1);
        document.getElementById("output").innerHTML = scr;
  
    function cls() {
        scr = "";
        document.getElementById("output").innerHTML = scr;
    }
</script>

<html> 
<head>
    <title>Binary Operations</title>
    <style type="text/css">
    body {margin: 30px;}
    </style> 
</head>
<body>

<form>
    <h1>Binary Search Operations</h1>
    <h2>perform binary operations "AND", "OR", "XOR", "Zero fill left shift", "Signed right shift", or "Zero fill right shift"<br></h2>
    1st Number: <input type="text" id="firstNumber"/><br>
    2nd Number: <input type="text" id="secondNumber"/><br>
    <input type="button" onClick="AND()" Value="AND"/>
    <input type="button" onClick="OR()" Value="OR"/>
    <input type="button" onClick="XOR()" Value="XOR"/>
    <input type="button" onClick="ZeroFillLeftShift()" Value="Zero fill left shift"/>
    <input type="button" onClick="SignedRightShift()" Value="Signed right shift"/>
    <input type="button" onClick="ZeroFillRightShift()" Value="Zero fill right shift"/>
</form>
    <p>The Result is: <br>
    <span id = "result2"></span>
</p>


<script>
    function AND() {
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        document.getElementById("result2").innerHTML = num1 & num2;
    }
    function OR() {
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        document.getElementById("result2").innerHTML = num1 | num2;
    }
    function XOR() {
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        document.getElementById("result2").innerHTML = num1 ^ num2;
    }
    function ZeroFillLeftShift() {
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        document.getElementById("result2").innerHTML = num1 << num2;
    }
    function SignedRightShift() {
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        document.getElementById("result2").innerHTML = num1 >> num2;
    }
    function ZeroFillRightShift() {
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        document.getElementById("result2").innerHTML = num1 >> num2;
    }
</script>

</body>
</html>



