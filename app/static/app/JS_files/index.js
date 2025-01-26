const header = document.querySelector(".calendar h3");
const dates = document.querySelector(".dates");
const navs = document.querySelectorAll("#prev, #next");

const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

let date = new Date();
let month = date.getMonth();
let year = date.getFullYear();

function renderCalendar() {
  const start = new Date(year, month, 1).getDay();
  const endDate = new Date(year, month + 1, 0).getDate();
  const end = new Date(year, month, endDate).getDay();
  const endDatePrev = new Date(year, month, 0).getDate();

  let datesHtml = "";

  for (let i = start; i > 0; i--) {
    datesHtml += `<li class="inactive">${endDatePrev - i + 1}</li>`;
  }

  for (let i = 1; i <= endDate; i++) {
    let className =
      i === date.getDate() &&
      month === new Date().getMonth() &&
      year === new Date().getFullYear()
        ? ' class="today"'
        : "";
    datesHtml += `<li${className}>${i}</li>`;
  }

  for (let i = end; i < 6; i++) {
    datesHtml += `<li class="inactive">${i - end + 1}</li>`;
  }

  dates.innerHTML = datesHtml;
  header.textContent = `${months[month]} ${year}`;
}

navs.forEach((nav) => {
  nav.addEventListener("click", (e) => {
    const btnId = e.target.id;

    if (btnId === "prev" && month === 0) {
      year--;
      month = 11;
    } else if (btnId === "next" && month === 11) {
      year++;
      month = 0;
    } else {
      month = btnId === "next" ? month + 1 : month - 1;
    }

    date = new Date(year, month, new Date().getDate());
    year = date.getFullYear();
    month = date.getMonth();

    renderCalendar();
  });
});

renderCalendar();




document.addEventListener('DOMContentLoaded', (event) => {
  let input = document.getElementById('inputBox');
  let calculatorButtons = document.querySelectorAll('.calc-button');
  let string = "";

  calculatorButtons.forEach(button => {
      button.addEventListener('click', (e) => {
          e.stopPropagation();
          if (e.target.innerHTML === '=') {
              try {
                  string = parseAndEvaluate(string);
              } catch (error) {
                  string = "Error";
              }
              input.value = string;
          }
          else if (e.target.innerHTML === 'AC') {
              string = "";
              input.value = string;
          }
          else if (e.target.innerHTML === 'D') {
              string = string.substring(0, string.length - 1);
              input.value = string;
          }
          else {
              string += e.target.innerHTML;
              input.value = string;
          }
      });
  });

  function parseAndEvaluate(expression) {
      let result = Function(`'use strict'; return (${expression})`)();
      return result;
  }
});


