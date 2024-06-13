const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			peoples: [],
			characters: [],
			card: [],
			people: [],
			favorites: [],
		},

		actions: {
		getCharacters: () => {
				// console.log("Estoy funcionando");
				fetch("https://urban-pancake-q77xv4jvrjwpc4vxq-3001.app.github.dev/api/people")
					.then(res => res.json())
					.then(data => setStore({ characters: data.results }))
					.catch(err => console.error(err))
			},

			signup: (name, email, password) => {
				return(
					fetch("https://urban-pancake-q77xv4jvrjwpc4vxq-3001.app.github.dev/signup", {
					method: 'POST', 
					headers: {"Content-Type": "application/json"}, 
					body: JSON.stringify({name: name, email: email, password: password})
				})
					.then(res => {
						if (!res.ok){
							throw Error()} 
							console.log("Hola");
						return res.json()
						})
					.then(data => data)
					.catch(err => console.error(err))
			)
			},

			login: (email, password, navigate) => {
				console.log(email, password);
				return(
					fetch("https://urban-pancake-q77xv4jvrjwpc4vxq-3001.app.github.dev/login", {
					method: 'POST', 
					headers: {"Content-Type": "application/json"}, 
					body: JSON.stringify({email: email, password: password})
				})
					.then(res => {
						if (!res.ok){
							throw Error()} 
						return res.json()
						})
					.then(data => {
						sessionStorage.setItem("token", data.access_token)
						navigate("/")
					})
					.catch(err => {console.error(err)
						return false
					}
				)
			)
			},

			getPeople: () => {
				fetch(`${process.env.BACKEND_URL}/api/people`, {
					method: 'GET'
				})
					.then(res => res.json())
					.then(data => setStore({ peoples: data.results }))
					.catch(err => console.error(err))
			},


			// cod error _pendiente revisar
			getFavorites: (setFavoritos) => {
				fetch(`${process.env.BACKEND_URL}api/user/favorites`, {
					method: 'GET',
					headers: {"Content-Type": "application/json",
					'Authorization': "Bearer "+ sessionStorage.getItem("token")
					}

				})
					.then(res => res.json())
					.then(data => {
						// setFavoritos(data.results);
						setStore({favorites:data.results})})
					.catch(err => console.error(err))
			},

			getPeopleDetails: (uid) => {
				// console.log("Mi tarjeta: " + card.name + " / Mi detalle: " + details.hair_color);
				fetch(`${process.env.BACKEND_URL}/api/people/${uid}`, {
					method: 'GET'
				})
					.then(res => res.json())
					.then(data => setStore({ people: data.result }))
					.catch(err => console.error(err))
			},

			addFavorite: (name) => {
				console.log("favorito a anyadir :" + name)
				const favoritesArr = [];
				getStore().favorites.map((elm) => {
					if (elm !== name) favoritesArr.push(elm);
				});
				favoritesArr.push(name);
				
				setStore({ 
					favorites: favoritesArr 
				});
				// setStore({ details: details });
			},

			deleteFavorite: (name) => {
				console.log("favorito a eliminar :" + name)
				const favoritesArr = [];
				getStore().favorites.map((elm, i) => {
					if (elm !== name) favoritesArr.push(elm);
				});
				
				setStore({ 
					favorites: favoritesArr 
				});
				// setStore({ details: details });
			},

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
		}
	};
};

export default getState;
