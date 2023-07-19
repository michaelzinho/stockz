import style from './style.module.css'
import Image from 'next/image';
import Home_icon from '../../../../public/home.svg'
import { Plus } from 'lucide-react'

export default function Home_left_nav_bar() {
  return (
    <div className={style.left_nav}>
      <Image className={style.home_icon} src={Home_icon} quality='100' alt="" width={60} height={50} />
      <Plus className={style.plus_icon} width={60} height={50} color='white'/>
    </div>
  )
}
