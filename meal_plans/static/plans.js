let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();
 
const calenderList = document.querySelector("#calendarList");
 
const currdate = document
    .querySelector(".calendar-current-date");
 
const prenexIcons = document
    .querySelectorAll(".calendar-navigation span");
 
// Array of month names
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
    "December"
];
 
// Function to generate the calendar
const updateCalendar = () => {
 
    // Get the first day of the month
    let dayone = new Date(year, month, 1).getDay();
 
    // Get the last date of the month
    let lastMonthDate = new Date(year, month + 1, 0).getDate();
 
    // Get the day of the last date of the month
    let dayend = new Date(year, month, lastdate).getDay();
 
    // Get the last date of the previous month
    let monthlastdate = new Date(year, month, 0).getDate();
 
    // Variable to store the generated calendar HTML
    let  = "";
 
    // Loop to add the last dates of the previous month
    for (let i = dayone; i > 0; i--) {
        htmlCalendar +=
            `<li class="pastDay">${monthlastdate - i + 1}</li>`;
    };

    for (let i = 1; i <= lastMonthDate; i++ ) {
        htmlCalendar +=
        `<li >${i}</li>`;
    };

    for (let i = dayend; i < 6; i--) {
        htmlCalendar +=
        `<li class="pastDay">${i}</li>`;
    }
    
}

updateCalendar();























 
// Attach a click event listener to each icon
// prenexIcons.forEach(icon => {
 
//     // When an icon is clicked
//     icon.addEventListener("click", () => {
 
//         // Check if the icon is "calendar-prev"
//         // or "calendar-next"
//         month = icon.id === "calendar-prev" ? month - 1 : month + 1;
 
//         // Check if the month is out of range
//         if (month < 0 || month > 11) {
 
//             // Set the date to the first day of the 
//             // month with the new year
//             date = new Date(year, month, new Date().getDate());
 
//             // Set the year to the new year
//             year = date.getFullYear();
 
//             // Set the month to the new month
//             month = date.getMonth();
//         }
 
//         else {
 
//             // Set the date to the current date
//             date = new Date();
//         }
 
//         // Call the manipulate function to 
//         // update the calendar display
//         manipulate();
//     });
// });