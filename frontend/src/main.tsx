import { createRoot } from 'react-dom/client'
import { BrowserRouter, Route, Routes } from 'react-router'

import Index from './pages/Index/Index'
import Login from './pages/Login/Login'
import AccountPage from './pages/Account/Account'

createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Index />} />
      <Route path='/login' element={<Login />} />
      <Route path='/account' element={<AccountPage />} />
    </Routes>
  </BrowserRouter>
)
