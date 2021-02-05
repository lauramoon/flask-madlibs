const url = new URL(window.location.href);
const title = url.searchParams.get('title');
const answerForm = document.querySelector('#answer-form');

function appendParams(params){
    for (param of params){
        const newDiv = document.createElement('div');
        newDiv.classList.add('prompt-div');
        const newHTML = `<label for="${param}">${param}:</label>
        <input class="form-element" id="${param}" type="text" name="${param}" autocomplete="off">`;
        newDiv.innerHTML = newHTML;
        answerForm.appendChild(newDiv);
    }
}

function addHiddenTemplate(text) {
    text = text.replace(/"/g, "'");
    console.log(text);
    const newDiv = document.createElement('div');
        newDiv.classList.add('template-div');
        const newHTML = `
        <input type="hidden" name="template" value="${text}">`;
        newDiv.innerHTML = newHTML;
        answerForm.appendChild(newDiv);
}

if (localStorage.getItem('savedTemplates')) {
    console.log('checking templates')
    const savedTemplates = JSON.parse(localStorage.getItem('savedTemplates'));
    for (template of savedTemplates) {
        console.log('template:', template)
        if (template.title === title) {
            console.log(template.params)
            appendParams(template.params);
            addHiddenTemplate(template.template);
        }
    }
}