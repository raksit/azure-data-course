import React from 'react'
import { Provider } from 'react-redux'
import { PersistGate } from 'redux-persist/integration/react'
import RootComponent from './RootComponent'
import { persistor, store } from './store/reducers/store'
import Header from './components/Header'
import Footer from './components/Footer'

const App: React.FC = () => {
    return (
        <Provider store={store}>
            <PersistGate loading={null} persistor={persistor}>
                <div className='container mt-5'>
                    <Header />
                    <main>
                        <RootComponent />
                    </main>
                    <Footer />
                </div>
            </PersistGate>
        </Provider>
    )
}

export default App
