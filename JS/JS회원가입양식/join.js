// 제출 이벤트를 받는다 (이벤트 핸들링)
const user_form = document.getElementById('user_form');
user_form.addEventListener('submit', function (event) {
    event.preventDefault(); // submit event 차단
    let user_id = event.target.id.value;
    let user_password = event.target.password.value;
    let user_password_c = event.target.password_check.value;
    let user_name = event.target.name.value;
    let user_phone_number = event.target.phone_number.value;
    let user_position = event.target.position.value;
    let user_gender = event.target.gender.value;
    let user_email = event.target.email.value;
    let user_intro = event.target.intro.value;

    // 제출된 입력 값들을 참조
    console.log(user_id, user_password, user_password_c, user_name, user_phone_number, user_position, user_gender, user_email, user_intro);

    // 입력값이 문제가 있는경우 감지
    if (user_password !== user_password_c) {
        alert('비밀번호와 비밀번호 확인이 불일치합니다')
        return
    }

    let p = document.createElement('p');
    p.innerHTML = `아이디 : ${user_id} <br> 이름 : ${user_name}<br> 전화번호 : ${user_phone_number}<br> 원하는 직무 : ${user_position}`;

    // 가입환영 인사를 제공
    let link = document.createElement('link');
    let div = document.createElement('div');

    div.id = "container";
    link.href = "css/user_form.css";
    link.rel = "stylesheet";

    document.write(`<h1>${user_name}님 환영합니다!<h1>`);
    document.body.appendChild(div);
    document.head.appendChild(link);

    document.querySelector("#container").appendChild(p);
})

