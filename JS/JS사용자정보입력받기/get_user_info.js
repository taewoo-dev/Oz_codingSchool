const user = document.querySelector("#user");
const user_name = document.querySelector("#user_name");
const habit = document.querySelector("#user_habit");
const fruit = document.querySelector("#user_favorite_fruit");
const animal = document.querySelector("#user_favorite_animal");

user_name.innerHTML = `이름 : <span>${prompt("이름을 입력하세요")}</span>입니다`;
habit.innerHTML = `저는 <span>${prompt('당신의 취미는?')}</span>를 좋아합니다.`;
fruit.innerHTML = `저는 과일 중에서 <span>${prompt("당신이 좋아하는 과일은?")}</span>를 제일 좋아합니다`;
animal.innerHTML = `저는 <span>${prompt('당신이 좋아하는 동물은?')}</span> 보는 것을 좋아합니다`;