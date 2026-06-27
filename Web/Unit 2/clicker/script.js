let numCookies = 0;
let cookiesPerClick = 0;
let cookiesPerSecond = 0;

let cookieDisplay = document.querySelector(".cookie_count");
let upgradesList = document.querySelector("#upgrades_list");
let cookieIncrement = 1;

// ======== frances click =====================================
const francesPic = document.querySelector("#frances"); 
document.querySelector(".frances_clicker").onClick = (ev) => {
    numCookies += cookieIncrement;
    // to add: animation that makes frances image bigger -> og size
}

// ======== manual click upgrade =====================================
let clonePrice = 25;
document.querySelector("#clones").onClick = (ev) => {
    if(numCookies >= clonePrice) {
        numCookies -= clonePrice
        cookieIncrement += clonePrice / 5;
        clonePrice *= 1.5;
    }
}

// ======== over-time upgrade =====================================
function upgradeCPS(price, productivity) {
    if (numCookies >= price) {
        numCookies -= price;
        cookiesPerSecond += productivity;
    }
}

let mainUpgradePrices = [50, 1000, 10000, 100000, 500000, 100000000];
let mainUpgradeProductivity = Array.from(mainUpgradePrices, (x) => 0.2 * x );
let mainUpgrades = Array.from(document.querySelectorAll(".main_upgrade"));
mainUpgrades.forEach((upgrade, index) => {
    let price = mainUpgradePrices[index];
    upgrade.onclick = function () {
        if (numCookies >= price) {
            numCookies -= price;
            cookiesPerSecond += mainUpgradeProductivity[index];
        }
    }
});

let secondaryUpgradePrices = [100, 5000, 50000, 250000, 10000000];
let secondaryUpgrades = Array.from(document.querySelectorAll(".secondary_upgrade"));
secondaryUpgrades.forEach((upgrade, index) => {
    let price = secondaryUpgradePrices[index];
    upgrade.onclick = function () {
        if (numCookies >= price) {
            numCookies -= price;
            mainUpgradeProductivity[index] *= 1.5;
            //to add: remove secondary upgrade from display
        }
    }
});

// pink jacket:
let jacketPrice = 100000000;
document.querySelector("#jacket").onClick = (ev) => {
    if(numCookies >= jacketPrice) {
        numCookies -= jacketPrice;
        // explode idk
    }
}

// ======== increment numCookies overtime + display numCookies + cookiesPerClick + cookiesPerSecond =====================================
function updateDisplay() {
    cookieDisplay.textContent = numCookies;
};

setInterval(() => {
    numCookies += cookiesPerSecond;
    updateDisplay();
}, 1000);

