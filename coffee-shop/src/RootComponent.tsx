import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import HomePage from './pages/HomePage'
import NotFoundPage from './pages/NotFoundPage'
import ShopDataDisplayPage from './pages/ShopDataPage'
import { ROUTES } from './resources/routes-constants'
import './styles/main.sass'

const RootComponent: React.FC = () => {
    return (
        <Router>
            <Routes>
                <Route path="*" element={<NotFoundPage />} />
                <Route path={ROUTES.HOMEPAGE_ROUTE} element={<HomePage />} />
                <Route path={ROUTES.SHOPDATADISPLAYPAGE_ROUTE} element={<ShopDataDisplayPage />} />
            </Routes>
        </Router>
    )
}

export default RootComponent
