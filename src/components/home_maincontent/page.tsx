import style from './style.module.css'
import Image from 'next/image';
import {LogOut, User } from 'lucide-react'
import Drive_icon from '../../../public/drive_icon.png'

export default function Drive_conection() {
  return (
    <div className={style.drive_box}>
      <div className={style.head}>
        <p className={[style.color_white, style.fontweight].join(" ")}>Google Drive</p>
        <div className={style.verification}></div>
      </div>
      
      <div className={style.image}>
          image
      </div>

      <div className={style.inf}>
        <div className={style.info}>
          <User  width={25} height={25} color='white'/>
          <p>`user@email.com`</p>
        </div>
        <LogOut  width={25} height={25} color='white'/>
      </div>
    </div>
  )
}
