import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import injectContext from "./store/appContext";
import { Navbar } from "./component/navbar.js";
import { Footer } from "./component/footer";
import { Signup } from "./component/signup.js";
// import { Login } from "../component/login.js";
import { Login } from "./pages/login.js";
import { Home } from "./pages/home.js";
import { DetailPeople } from "./pages/detailpeople.js";


const Layout = () => {
	const basename = process.env.BASENAME || "";

	return (
		<div>
			<BrowserRouter basename={basename}>
				<ScrollToTop>
					<Navbar />
					<Routes>
						<Route path="/" element={<Home />} />
						<Route path="/signup" element={<Signup />} />
						<Route path="/login" element={<Login />} />
						<Route path="/detailpeople/:uid" element={<DetailPeople />} />
						<Route path="*" element={<h1>Not found!</h1>} />
					</Routes>
					<Footer />
				</ScrollToTop>
			</BrowserRouter>
		</div>
	);
};

export default injectContext(Layout);
