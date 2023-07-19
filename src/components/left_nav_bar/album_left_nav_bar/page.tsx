import style from './style.module.css'
import Image from 'next/image';
import Link from 'next/link'
import Album_icon from '../../../../public/albuns.svg'
import { Plus } from 'lucide-react'

export default function Album_left_nav_bar() {
  return (
    <div className={style.left_nav}>
      <Image className={style.home_icon} src={Album_icon} quality='100' alt="" width={60} height={50} />
      <Link href="create_album"><Plus className={style.plus_icon} width={60} height={50} color='white'/></Link>
      
    </div>
  )
}
