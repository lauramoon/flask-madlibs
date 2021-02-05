const titleList = document.querySelector('#title-selection')

if (localStorage.getItem('savedTemplates')) {
    const savedTemplates = JSON.parse(localStorage.getItem('savedTemplates'));
    for (template of savedTemplates) {
        const newOption = document.createElement('option');
        newOption.innerText = template.title;
        newOption.nodeValue = template.title;
        titleList.appendChild(newOption);
    }
}