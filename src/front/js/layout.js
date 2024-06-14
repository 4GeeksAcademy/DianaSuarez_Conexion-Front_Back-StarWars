import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";
import { Navbar } from "./component/navbar.js";
import { Footer } from "./component/footer";
import { Signup } from "./pages/signup.js";
import { Login } from "./pages/login.js";
import { Home } from "./pages/home.js";
import { DetailPeople } from "./pages/detailpeople.js";
import injectContext from "./store/appContext";

const Layout = () => {
	const basename = process.env.BASENAME || "";

	if(!process.env.BACKEND_URL || process.env.BACKEND_URL == "") return <BackendURL/ >;

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
