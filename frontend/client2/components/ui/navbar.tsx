"use client";

import { cn } from "@/lib/utils/util";
import { UserButton } from "@clerk/nextjs";
import { Menu, Sparkles } from "lucide-react";
import { Poppins } from "next/font/google";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ModeToggle } from './theme-toggle';
import { MobileSidebar } from '@/components/mobile-sidebar';

const font = Poppins({
  weight: "600",
  subsets: ["latin"],
});

export default function Navbar() {
  return (
    <div className="fixed w-full z-50 flex justify-between items-center py-2 px-4 border-b border-primary/10 bg-slate-800 h-16">
      <div className="flex items-center">
        <MobileSidebar />
        <Link href="/">
          <h1
            className={cn(
              "hidden md:block uppercase text-xl text-gray-300 font-bold",
              font.className
            )}
          >
            a<span className="text-orange-500">w</span>ahss
          </h1>
        </Link>
      </div>
      <div className="flex items-center gap-x-3">
        <Button size="sm">
          Upgrade
          <Sparkles className="h-4 w-4 fill-white ml-2" />
        </Button>
         <ModeToggle />
        <UserButton />
      </div>
    </div>
  );
}
