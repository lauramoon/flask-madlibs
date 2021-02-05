const newTemplateForm = document.querySelector('#new-template-form');
const deleteTemplatesButton = document.querySelector('#delete-local-templates');
const titleField = document.querySelector('#title');
const templateField = document.querySelector('#new-template');

function parseTemplate(template) {
    console.log(template);
    const params = new Array();
    let param = "";
    let in_param = false
    for (char of template) {
        if (char === '}') {
            params.push(param);
            param = "";
            in_param = false;

        } else if (in_param) {
            param += char
        } else if (char === '{') {
            in_param = true;
        }
    }
    return params;
}

function addToLocalStorage(params, template, title) {
    const templateJSON = {
        title,
        params,
        template
    }
    let savedTemplates;
    if (localStorage.getItem('savedTemplates')) {
        savedTemplates = JSON.parse(localStorage.getItem('savedTemplates'));
        const titleList = savedTemplates.map((template) => template.title)
        if (titleList.includes(title)) {
            alert("A story with that title already exists. Please try another title.");
        } else {
            savedTemplates.push(templateJSON);
            alert("Template saved. Click 'New Story' to try it out.");
        }
    } else {
        savedTemplates = [templateJSON];
        alert("Template saved. Click 'New Story' to try it out.");
    }

    localStorage.setItem('savedTemplates', JSON.stringify(savedTemplates));
}


newTemplateForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const title = titleField.value;
    const new_template = templateField.value;

    try {
        console.log(title, new_template);
        const params = parseTemplate(new_template);
        addToLocalStorage(params, new_template, title);
        titleField.value = "";
        templateField.value = "";
    } catch(e) {
        console.log(e);
        alert ('Unable to parse template. Please try again.')
    }
})

deleteTemplatesButton.addEventListener('click', function(e) {
    if (confirm('Are you sure you want to delete your templates?')) {
        localStorage.removeItem('savedTemplates');
    }
    
})
