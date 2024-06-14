const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			people: [],
			peoples: []
		},

		actions: {
			getMessage: async () => {
				try {
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},			
		
		login: async (email, password) => {
			try {
			const response = await fetch(`${process.env.BACKEND_URL}/api/login`, {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({
						email: email,
						password: password
					})
				});
				let data = await response.json()
				if (response.status === 200) {
					localStorage.setItem("token", data.access_token);
					return true;
				} else {
					return false
				}
			} catch (error) {
				return false;
			}
		},

		logOut: () => {
			localStorage.removeItem('token');
			setStore({ 
				favorites: [],
				myPeople: [] 
			});
		},

		signup: async (email, password) => {
                try {
					const response = await fetch(`${process.env.BACKEND_URL}/api/signup`, {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json'
						},
						body: JSON.stringify({
							email: email,
							password: password
						})
					});
					let data = await response.json()
					if (response.status === 201) {
						localStorage.setItem("token", data.access_token);
						return "success";
					} else if (response.status === 409) {
						return "email_exist";
					} else {
						return "incomplete_data"
					}
				} catch (error) {
					return false;
				}
			},		
			isAuthenticated: (token) => {
				const options = {
					method: 'POST',
					headers: {
						"Content-Type": "application/json",
						"Authorization": 'Bearer ' + token
					},
					body: JSON.stringify({})
				};
				fetch(process.env.BACKEND_URL + "/api/private", options)
					.then(response => {
						if (response.status === 200) {
							return response.json();
						} else {
							throw new Error("Hubo un problema en la solicitud de inicio de sesión");
						}
					})
					.then(data => {
						setStore({ storeToken: true });
					})	
					.catch(error => console.log('error', error));
			},
		}
	};
};
export default getState;