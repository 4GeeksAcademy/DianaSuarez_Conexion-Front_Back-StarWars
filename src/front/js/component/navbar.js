import React, { useContext, useEffect, useState} from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext.js";

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	const [favoritos, setFavoritos]= useState(store.favorites)
	console.log(store.favorites);
	useEffect(() =>{
		if (sessionStorage.getItem("token")) {
			actions.getFavorites(setFavoritos)
		}
	},[] )
console.log(favoritos);
	return (
		<nav className="navbar navbar-light bg-secondary mb-4">
			<Link to="/">
				<span className="navbar-brand ms-5"></span>
				<img src="https://i.pinimg.com/originals/b4/b5/fd/b4b5fdf7bf06601ad4bd1cc6f73acff3.png" style={{ width: "7rem" }} />
			</Link>
			<div className="ml-auto d-flex">
				{/* <!-- Example single danger button --> */}
				<div className="btn-group me-5">
				<button type="submit" className="btn btn-primary">Submit</button>
            <Link to={'/login'}>
                <button type="submit" className="btn btn-primary">Login</button>
            </Link>
			{store.favorites?.length >0 && (
				<>
				<button type="button" className="btn btn-primary d-flex rounded" 
						data-bs-toggle="dropdown" aria-expanded="false">Favorites
						<div className="contador px-1 bg-secundary"><span>{favoritos.length}</span></div>
						<div className= "dropdown-toggle px-1"></div>
					</button>
					<ul className="dropdown-menu">
						{store.favorites.map((item) => {
							return (
								<li className="d-flex">
									<a className="dropdown-item">{item.name}</a>
									<span className="delete" onClick={() => actions.deleteFavorite(item)}>
										<i className="fas fa-trash-alt me-2"></i>
									</span>
								</li>
							)
						})}
					</ul>
					</>
			)}
				</div>
			</div>
		</nav>
















		// <nav className="navbar navbar-light bg-light mb-3 - p-4">
		// 	<Link to="/">
		// 		<span className="navbar-brand mb-0 h1">React Boilerplate</span>
		// 	</Link>
		// 	<div className="ml-auto">
		// 		<Link to="/home">
		// 			<button className="btn btn-primary">Favorites</button>
		// 		</Link>
		// 	</div>
		// </nav>
	);
};
