let logoutLink = document.getElementById('logout-link');
let deleteLink = document.getElementById('delete-link');

logoutLink.addEventListener('click', async (event) =>
{
    let message = 'Вы собираетесь выйти из аккаунта.';

    if (!confirm(message))
    {
        event.preventDefault();
    }
});

deleteLink.addEventListener('click', async (event) =>
{
    let message = 'Вы собираетесь удалить объект.';

    if (!confirm(message))
    {
        event.preventDefault();
    }
});
