function responsive() {
	var response = document.getElementById("myTopnav");
	if (response.className === "topnav") {
		response.className += " responsive";
	} else {
		response.className = "topnav";
	}
}

var selectItem = {
	"total": 0,
	"lastTransactionAmount": 0,
	"max": 20,
	//adding items
	"add": function (itemCost) {
		this.total += itemCost;
		this.lastTransactionAmount = itemCost;
	},
	//scanning items
		"scan": function (item) {
			var id = '#' + item;
			var quantity = $(id).val();
			var rentFee = 100;
			var tax = 1.07;
			var deposit = 10;
			var max = 20;
		switch (item) {
			case "Casual":
				this.add(120 / deposit * quantity + rentFee * tax);
				new_max = max - quantity;
				document.getElementById('Casual').setAttribute("max", new_max);
				break;
			case "Cocktail":
				this.add(100 / deposit * quantity + rentFee * tax);
				break;
			case "Evening":
				this.add(175 / deposit * quantity + rentFee * tax);
				break;
			case "Pageant":
				this.add(150 / deposit * quantity + rentFee * tax);
				break;
			case "Prom":
				this.add(200 / deposit * quantity + rentFee * tax);
				break;
			case "Wedding":
				this.add(300 / deposit * quantity + rentFee * tax);
				break;
		}
	},
}

function rentItem() {
	document.getElementById('rent').innerHTML = "Your total is: $" + selectItem.total.toFixed(2);
}

var myIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("animate-fading");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
    }
    myIndex++;
    if (myIndex > x.length) {myIndex = 1}    
    x[myIndex-1].style.display = "block";  
    setTimeout(carousel, 4000);    
}