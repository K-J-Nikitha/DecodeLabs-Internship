const API = "/users";

const form = document.getElementById("userForm");
const table = document.getElementById("userTable");

// Load all users when page loads
window.onload = loadUsers;


// ---------------- LOAD USERS ---------------- //

async function loadUsers() {

    try {

        const response = await fetch(API);

        const users = await response.json();

        table.innerHTML = "";

        if (users.length === 0) {

            table.innerHTML = `
                <tr>
                    <td colspan="7" class="empty-message">
                        No Users Found
                    </td>
                </tr>
            `;

            return;
        }

        users.forEach(user => {

            table.innerHTML += `

            <tr>

                <td>${user.id}</td>

                <td>${user.name}</td>

                <td>${user.email}</td>

                <td>${user.age}</td>

                <td>

                    ${
                        user.is_active
                        ?
                        '<span class="badge-active">Active</span>'
                        :
                        '<span class="badge-inactive">Inactive</span>'
                    }

                </td>

                <td>${formatDate(user.created_at)}</td>

                <td>

                    <button
                        class="edit-btn"
                        onclick="editUser(${user.id},
                        '${user.name}',
                        '${user.email}',
                        ${user.age})">

                        Edit

                    </button>

                    <button
                        class="delete-btn"
                        onclick="deleteUser(${user.id})">

                        Delete

                    </button>

                </td>

            </tr>

            `;

        });

    }

    catch (error) {

        console.error(error);

        alert("Unable to load users.");

    }

}



// ---------------- ADD USER ---------------- //

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const name = document.getElementById("name").value.trim();

    const email = document.getElementById("email").value.trim();

    const age = document.getElementById("age").value;

    const response = await fetch(API, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            name,

            email,

            age

        })

    });

    if (response.status === 409) {

        alert("Email already exists.");

        return;

    }

    if (!response.ok) {

        alert("Unable to add user.");

        return;

    }

    form.reset();

    loadUsers();

});



// ---------------- DELETE USER ---------------- //

async function deleteUser(id) {

    const confirmDelete = confirm(

        "Are you sure you want to delete this user?"

    );

    if (!confirmDelete) return;

    await fetch(API + "/" + id, {

        method: "DELETE"

    });

    loadUsers();

}



// ---------------- EDIT USER ---------------- //

async function editUser(id, name, email, age) {

    const newName = prompt("Enter Name", name);

    if (newName === null) return;

    const newEmail = prompt("Enter Email", email);

    if (newEmail === null) return;

    const newAge = prompt("Enter Age", age);

    if (newAge === null) return;

    const response = await fetch(API + "/" + id, {

        method: "PUT",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            name: newName,

            email: newEmail,

            age: newAge

        })

    });

    if (response.status === 409) {

        alert("Email already exists.");

        return;

    }

    if (!response.ok) {

        alert("Unable to update user.");

        return;

    }

    loadUsers();

}



// ---------------- DATE FORMAT ---------------- //

function formatDate(date) {

    if (!date) return "-";

    return new Date(date).toLocaleString();

}
